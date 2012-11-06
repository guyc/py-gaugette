import gaugette.oauth
import datetime

CLIENT_ID       = 'your client_id here'
CLIENT_SECRET   = 'your client secret here'
SPREADSHEET_KEY = 'your spreadsheet key here'

oauth = gaugette.oauth.OAuth(CLIENT_ID, CLIENT_SECRET)
if not oauth.has_token():
    user_code = oauth.get_user_code()
    print "Go to %s and enter the code %s" % (oauth.verification_url, user_code)
    oauth.get_new_token()

gd_client = oauth.spreadsheet_service()
spreadsheet_id = SPREADSHEET_KEY
worksheets_feed = gd_client.GetWorksheetsFeed(spreadsheet_id)
print worksheets_feed
worksheet_id = worksheets_feed.entry[0].id.text.rsplit('/',1)[1]
print worksheet_id

now = datetime.datetime.now().isoformat(' ')
row = {
    'project': 'datatest',
    'start'  : now,
    'finish' : now
    }

gd_client.InsertRow(row, spreadsheet_id, worksheet_id)
