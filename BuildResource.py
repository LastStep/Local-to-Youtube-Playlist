from apiclient.discovery import build
from google.oauth2.credentials import Credentials
import json

def run():

    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'

    with open('-oauth2.json') as f:
        credentials = json.load(f)

    credentials = Credentials(
        token = credentials['access_token'],
        refresh_token = credentials['refresh_token'],
        token_uri = credentials['token_uri'],
        client_id = credentials['client_id'],
        client_secret = credentials['client_secret']
    )

    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


