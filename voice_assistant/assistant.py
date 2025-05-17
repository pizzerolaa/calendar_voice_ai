from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

from config.settings import API_KEY, AGENT_ID, ASSISTANT_NAME, USER_NAME
from data_sources.calendar_integration import get_todays_events, format_events_for_assistant

class VoiceAssistant:
    def __init__(self):
        """Initialize voice assistant with calendar integration."""
        self.user = USER_NAME
        self.client = ElevenLabs(api_key=API_KEY)

        events = get_todays_events()
        self.schedule = format_events_for_assistant(events)

        self._setup_assistant()
    
    def _setup_assistant(self):
        """Configure assistant and conversation."""
        prompt = f'You are a personal assistant named {ASSISTANT_NAME}. Your contact is called {self.user} and has the following schedule for today: {self.schedule}.'
        first_msg = f'Hi {self.user}, Im {ASSISTANT_NAME}. How can I help you today?'

        conv_override = {
            'agent': {
                'prompt': {
                    'prompt': prompt,
                },
                'first_message': first_msg,
            },
        }

        self.config = ConversationConfig(
            conversation_config_override = conv_override,
            extra_body = {},
            dynamic_variables = {},
        )

        self.conversation = Conversation(
            self.client,
            AGENT_ID,
            config=self.config,
            requires_auth=True,
            audio_interface=DefaultAudioInterface(),
            callback_agent_response=self._print_ai_response,
            callback_agent_response_correction=self._print_interrupted_response,
            callback_user_transcript=self._print_user_transcript,
        )
    
    def _print_ai_response(self, response):
        """Displays the assistant response."""
        print(f"{ASSISTANT_NAME}: {response}")
    
    def _print_interrupted_response(self, original, corrected):
        """Handles interruptions during the assistant's response."""
        print(f"{ASSISTANT_NAME} interrupted, truncated response: {corrected}")
    
    def _print_user_transcript(self, transcript):
        """Displays the transcript of what the user says."""
        print(f"{self.user}: {transcript}")
    
    def start(self):
        """Start the chat session."""
        print(f"Starting {ASSISTANT_NAME}...")
        self.conversation.start_session()