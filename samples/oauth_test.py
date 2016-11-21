from gaugette.oauth import DeviceOAuth
from apiclient import discovery
import datetime
import httplib2
import base64
import json

# Beyond testing, generate your own client_id and secret
client_id       = '911969952744.apps.googleusercontent.com'
client_secret   = 'fj7nrIP3AeYDFQDbewnWrmfM'
# only pass the scope or scopes you require.
scopes          = ['profile', 'email', 'https://www.googleapis.com/auth/calendar.readonly']

# show_user_code is called from oauth_get_token to present the code to the user
def show_user_code(user_code, verification_url):
    print("Go to %s and enter the code %s" % (verification_url, user_code))

# for scopes like profile and email we will get back an jwt token 'id_token'
# that can be parsed to get the identity details.
def parse_token(token):
    parts = token.split('.')
    if len(parts) == 3:
        payload = base64.b64decode(parts[1])
        return json.loads(payload.decode())

# initialise the oauth class
oauth = DeviceOAuth(client_id, client_secret, scopes)

# if token.json doesn't exist, a new token will be fetched and the
# callback 'show_user_code' will be called to get user verification.
token = oauth.get_token(show_user_code)
print("token: %s", token)
if token['id_token']:
    data = parse_token(token['id_token'])
    if data:
        print(json.dumps(data, indent=2))

# To use the token to call a google API, use oauth.get_credentials
# and credentials.authorize to bind the credentials to http client.
# This will pass along the bearer token on each request.
# You may get an error promting you to enable calendar access via the developers console
credentials = oauth.get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('calendar', 'v3', http=http)
result = service.events().list(calendarId='primary').execute()
print(json.dumps(result, indent=2))
print("done")
