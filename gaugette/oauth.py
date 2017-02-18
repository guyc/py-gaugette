# https://developers.google.com/accounts/docs/OAuth2ForDevices

import sys
import urllib
import httplib2
import os.path
import json
import time
from oauth2client import client
from datetime import datetime, timedelta

class DeviceOAuth:

    def __init__(self, client_id, client_secret, scopes):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self.retry_interval = 10 # will be set by get_user_code
        self.device_code = None
        self.verification_url = None
        self.user_code = None
        self.conn = None
        self.token_file = 'oauth_token.json'
        self.scope = scopes
        self.reset_connection()


    def get_token(self, on_user_code):
        token = self.load_token()
        if token == None:
            user_code = self.get_user_code()
            on_user_code(user_code, self.verification_url) # prompt user
            token = self.get_new_token()
        return token

    def get_credentials(self):
        isoFormat = "%Y-%m-%dT%H:%M:%S.%f"
        access_token = self.token['access_token']
        refresh_token = self.token['refresh_token']
        expires_at = datetime.strptime(self.token['expires_at'], isoFormat)
        token_uri = 'https://accounts.google.com/o/oauth2/token'
        user_agent = 'gaugette/1.0'
        credentials = client.GoogleCredentials(access_token, self.client_id, self.client_secret, refresh_token, expires_at, token_uri, user_agent)
        return credentials

    # this setup is isolated because it eventually generates a BadStatusLine
    # exception, after which we always get httplib.CannotSendRequest errors.
    #  When this happens, we try re-creating the exception.
    def reset_connection(self):
        # httplib.HTTPConnection.debuglevel = 1
        self.conn = httplib2.Http()

    def load_token(self):
        self.token = None
        if os.path.isfile(self.token_file):
            with open(self.token_file) as file:
                self.token = json.load(file)
        return self.token

    def save_token(self):
        with open(self.token_file, 'w') as file:
            file.write(json.dumps(self.token))

    def has_token(self):
        return self.token != None

    def get_user_code(self):
        (response, content) = self.conn.request(
            "https://accounts.google.com/o/oauth2/device/code",
            "POST",
            urllib.parse.urlencode({
                'client_id': self.client_id,
                'scope'    : ' '.join(self.scope)
                }),
            {"Content-type": "application/x-www-form-urlencoded"}
            )

        content_utf8 = content.decode('utf-8')

        if response.status == 200:
            data = json.loads(content_utf8)
            self.device_code = data['device_code']
            self.user_code = data['user_code']
            self.verification_url = data['verification_url']
            self.retry_interval = data['interval']
        else:
            print(response.status)
            print(content)
            sys.exit()
        return self.user_code

    def set_token_expiry(self):
        expires_in = timedelta(seconds=self.token['expires_in'])
        expires_at = datetime.now() + expires_in
        self.token['expires_at'] = expires_at.isoformat()

    def get_new_token(self):

        while self.token == None:
            (response, content) = self.conn.request(
                "https://accounts.google.com/o/oauth2/token",
                "POST",
                urllib.parse.urlencode({
                    'client_id'     : self.client_id,
                    'client_secret' : self.client_secret,
                    'code'          : self.device_code,
                    'grant_type'    : 'http://oauth.net/grant_type/device/1.0'
                    }),
                {"Content-type": "application/x-www-form-urlencoded"}
                )

            content_utf8 = content.decode('utf-8')

            if response.status == 200:
                data = json.loads(content_utf8)
                if 'access_token' in data:
                    self.token = data
                    self.set_token_expiry()
                    self.save_token()
                else:
                    time.sleep(self.retry_interval + 2)
        return self.token

    def refresh_token(self):
        refresh_token = self.token['refresh_token']
        self.conn.request(
            "POST",
            "/o/oauth2/token",
            urllib.parse.urlencode({
                'client_id'     : self.client_id,
                'client_secret' : self.client_secret,
                'refresh_token' : refresh_token,
                'grant_type'    : 'refresh_token'
                }),
            {"Content-type": "application/x-www-form-urlencoded"}
            )

        response = self.conn.getresponse()
        if response.status == 200:
            data = json.loads(response.read())
            if 'access_token' in data:
                self.token = data
                # we NEVER get a new refresh token at this point
                self.token['refresh_token'] = refresh_token
                self.set_token_expiry()
                self.save_token()
                return True
        else:
            print("Unexpected response %d to renewal request" % response.status)
            print(response.read())
        return False
