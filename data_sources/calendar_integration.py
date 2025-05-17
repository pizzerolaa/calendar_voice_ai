import os
import datetime
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from config.settings import CREDENTIALS_FILE, SCOPES

def get_calendar_serv():
    """Gets an Google Calendar auth service."""
    credentials = None
    token_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'token.pickle')

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            credentials = pickle.load(token)
    
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            # Intenta con diferentes puertos conocidos
            ports = [8080, 8090, 8000]
            success = False
            
            for port in ports:
                try:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        CREDENTIALS_FILE, 
                        SCOPES,
                        redirect_uri=f'http://localhost:{port}'
                    )
                    credentials = flow.run_local_server(port=port)
                    success = True
                    break
                except Exception as e:
                    print(f"Error con puerto {port}: {e}")
                    continue
            
            if not success:
                # Si ningún puerto conocido funciona, intenta el método predeterminado
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                credentials = flow.run_local_server(port=0)
        
        with open(token_path, 'wb') as token:
            pickle.dump(credentials, token)
    return build('calendar', 'v3', credentials=credentials)

def get_todays_events():
    """Get calendar evants for current day"""
    service = get_calendar_serv()

    calendar_list = service.calendarList().get(calendarId='primary').execute()
    timezone = calendar_list['timeZone']

    now = datetime.datetime.now(datetime.timezone.utc).astimezone()
    start_of_day = datetime.datetime(now.year, now.month, now.day, 0, 0, 0, tzinfo=now.tzinfo)
    end_of_day = datetime.datetime(now.year, now.month, now.day, 23, 59, 59, tzinfo=now.tzinfo)

    start_str = start_of_day.isoformat()
    end_str = end_of_day.isoformat()

    events_result = service.events().list(
        calendarId='primary',
        timeMin=start_str,
        timeMax=end_str,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    return events_result.get('items', [])

def format_events_for_assistant(events):
    """Format events so that the assistant to communicate"""
    if not events:
        return "No tienes eventos programados para hoy"

    formatted_schedule = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_time = datetime.datetime.fromisoformat(start)
        event_time = start_time.strftime("%H:%M")
        formatted_schedule.append(f"{event['summary']} a las {event_time}")
    
    return "; ".join(formatted_schedule)