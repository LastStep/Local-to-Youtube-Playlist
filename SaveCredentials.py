from google_auth_oauthlib.flow import InstalledAppFlow
from apiclient.discovery import build

def run():
	
	SCOPES = ['https://www.googleapis.com/auth/youtube']
	API_SERVICE_NAME = 'youtube'
	API_VERSION = 'v3'
	
	CLIENT_SECRETS_FILE = "client_secret.json"
	
	flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
	credentials = flow.run_console()
	
	youtube = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
	
	return youtube