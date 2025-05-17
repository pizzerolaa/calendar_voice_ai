# Voice Assistant with Google Calendar Integration

This project builds an interactive voice assistant powered by ElevenLabs API with Google Calendar integration. It was inspired by the [Codedex Voice Virtual Assistant project](https://www.codedex.io/projects/create-a-voice-virtual-assistant-with-elevenlabs) with significant enhancements to create a more practical, everyday assistant.

## Features

- **Voice-based interaction** - Talk to the assistant and receive spoken responses
- **Calendar integration** - Access your Google Calendar events for the current day
- **Personalized experience** - Assistant knows your name and provides tailored responses
- **Intelligent conversation** - Powered by ElevenLabs conversational AI

## Project Structure

```
python_project/
├── config/
│   └── settings.py           # Centralized configuration
├── data_sources/
│   ├── __init__.py
│   ├── calendar_integration.py  # Google Calendar API integration
│   └── calendar_utils.py     # Helper functions for calendar events
├── voice_assistant/
│   ├── __init__.py
│   ├── assistant.py          # Main assistant class
│   └── conversation.py       # Conversation handling
├── app.py                    # Main entry point
├── requirements.txt          # Project dependencies
├── credentials.json          # Google OAuth credentials (not in repo)
└── .env                      # Environment variables for API keys (not in repo)
```

## Prerequisites

1. **ElevenLabs Account**
   - Sign up at [ElevenLabs](https://elevenlabs.io/)
   - Create a conversational agent and get your Agent ID
   - Generate an API key

2. **Google Cloud Project**
   - Create a project in [Google Cloud Console](https://console.cloud.google.com/)
   - Enable the Google Calendar API
   - Create OAuth 2.0 credentials (download as credentials.json)
   - Configure the OAuth consent screen
   - Add authorized redirect URIs (http://localhost:8080/, http://localhost:8090/, http://localhost:8000/)

## Setup Instructions

1. **Clone the repository**
   ```
   git clone https://github.com/pizzerolaa/calendar_voice_ai.git
   cd python_project
   ```

2. **Create virtual environment**
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a .env file in the root directory:
   ```
   AGENT_ID=your_elevenlabs_agent_id
   API_KEY=your_elevenlabs_api_key
   GOOGLE_API_KEY=your_google_apikey
   ```

5. **Add Google credentials**
   - Place your credentials.json file in the root directory

## Running the Assistant

Run the application:
```
python app.py
```

On first run:
1. A browser window will open requesting authorization to access your Google Calendar
2. Grant the necessary permissions
3. The assistant will start and greet you
4. Speak with the assistant - it will respond through your speakers

## Authentication Troubleshooting

If you encounter OAuth errors:
1. Verify that your credentials.json file is valid and placed in the correct location
2. Ensure all required redirect URIs are registered in Google Cloud Console
3. Delete the token.pickle file (if it exists) to force a new authentication
4. Verify that your account is added as a test user if the application is in testing mode

## Future Enhancements

- Integration with additional data sources (weather, news, etc.)
- Task management capabilities
- Custom voice and personality settings
- Mobile application integration
- Multi-calendar support

## Technology Stack

- **Python** - Core programming language
- **ElevenLabs API** - Voice synthesis and conversational AI
- **Google Calendar API** - Calendar data source
- **OAuth 2.0** - Authentication with Google services

## Acknowledgements

This project was built upon the foundation provided by [Codedex's Voice Virtual Assistant tutorial](https://www.codedex.io/projects/create-a-voice-virtual-assistant-with-elevenlabs), with significant enhancements for Google Calendar integration and improved architecture.

---

*Note: This project is for educational purposes. Be mindful of API usage limits and associated costs with ElevenLabs.*