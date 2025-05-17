import os
from dotenv import load_dotenv

load_dotenv()

AGENT_ID = os.getenv('AGENT_ID')
API_KEY = os.getenv('API_KEY')

GOOGLE_API = os.getenv('GOOGLE_API_KEY')
CREDENTIALS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'credentials.json')

USER_NAME = 'Fher'

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

ASSISTANT_NAME = 'Jarvis'