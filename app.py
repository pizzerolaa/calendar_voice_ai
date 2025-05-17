from voice_assistant.assistant import VoiceAssistant

def main():
    """Main function that starts the voice assistant."""
    assistant = VoiceAssistant()
    try:
        assistant.start()
    except KeyboardInterrupt:
        print("\nUser-terminated assistant")

if __name__ == "__main__":
    main()