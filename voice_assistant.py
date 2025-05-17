import os
from dotenv import load_dotenv

load_dotenv()

AGENT_ID = os.getenv('AGENT_ID')
API_KEY = os.getenv('API_KEY')
GOOGLE_API = os.getenv('GOOGLE_API_KEY')