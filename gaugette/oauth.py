# https://developers.google.com/accounts/docs/OAuth2ForDevices

import sys
import urllib
try:
    import httplib # python2
except ImportError:
    import http.client # python3
import os.path
import json
import time
import gdata.spreadsheet.service
import gdata.docs.service

class OAuth:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self.device_code = None
        self.verfication_url = None
        self.token_file = 'oauth_token.json'
        self.scope = [
            'https://spreadsheets.google.com/feeds', #  scope information for the Google Spreadsheets API
            'https://docs.google.com/feeds',         # if an application needs to create spreadsheets, or otherwise manipulate their metadata,
        ]
        self.host = 'accounts.google.com'
        self.reset_connection()
        self.load_token()

    # this setup is isolated because it eventually generates a BadStatusLine
    # exception, after which we always get httplib.CannotSendRequest errors.
    #  When this happens, we try re-creating the exception.
    def reset_connection(self):
        # httplib.HTTPConnection.debuglevel = 1
        self.conn = httplib.HTTPSConnection(self.host)

    def load_token(self):
        token = None
        if os.path.isfile(self.token_file):
            f = open(self.token_file)
            json_token = f.read()
            self.token = json.loads(json_token)
            f.close()

    def save_token(self):
        f = open(self.token_file, 'w')
        f.write(json.dumps(self.token))
        f.close()

    def has_token(self):
        return self.token != None

    def get_user_code(self):
        self.conn.request(
            "POST",
            "/o/oauth2/device/code",
            urllib.urlencode({
                'client_id': self.client_id,
                'scope'    : ' '.join(self.scope)
                }),
            {"Content-type": "application/x-www-form-urlencoded"}
            )
        response = self.conn.getresponse()
        if (response.status == 200):
            data = json.loads(response.read())
            self.device_code = data['device_code']
            self.user_code = data['user_code']
            self.verification_url = data['verification_url']
            self.retry_interval = data['interval']
        else:
            print(response.status)
            print(response.read())
            sys.exit()
        return self.user_code
    
    def get_new_token(self):
        # call get_device_code if not already set
        if not self.user_code:
            self.get_user_code()
            
        while self.token == None:
            self.conn.request(
                "POST",
                "/o/oauth2/token",
                urllib.urlencode({
                    'client_id'     : self.client_id,
                    'client_secret' : self.client_secret,
                    'code'          : self.device_code,
                    'grant_type'    : 'http://oauth.net/grant_type/device/1.0'
                    }),
                {"Content-type": "application/x-www-form-urlencoded"}
                )

            response = self.conn.getresponse()
            if (response.status == 200):
                data = json.loads(response.read())
                # print data
                if 'access_token' in data:
                    self.token = data
                    self.save_token()
                else:
                    time.sleep(self.retry_interval + 2)

    def refresh_token(self):
        refresh_token = self.token['refresh_token']
        self.conn.request(
            "POST",
            "/o/oauth2/token",
            urllib.urlencode({
                'client_id'     : self.client_id,
                'client_secret' : self.client_secret,
                'refresh_token' : refresh_token,
                'grant_type'    : 'refresh_token'
                }),
            {"Content-type": "application/x-www-form-urlencoded"}            
            )

        response = self.conn.getresponse()
        if (response.status == 200):
            data = json.loads(response.read())
            if 'access_token' in data:
                self.token = data
                # in fact we NEVER get a new refresh token at this point
                if not 'refresh_token' in self.token:
                    self.token['refresh_token'] = refresh_token
                    self.save_token()
                return True
        else:
            print("Unexpected response %d to renewal request" % response.status)
            print(response.read())
        return False
              
    def spreadsheet_service(self):
        headers = {
            "Authorization": "%s %s" % (self.token['token_type'], self.token['access_token'])
        }
        client = gdata.spreadsheet.service.SpreadsheetsService(additional_headers=headers)
        return client

    def docs_service(self):
        headers = {
            "Authorization": "%s %s" % (self.token['token_type'], self.token['access_token'])
        }
        client = gdata.docs.service.DocsService(additional_headers=headers)
        return client
        
