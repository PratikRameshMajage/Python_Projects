import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set voice properties
# List available voices: engine.getProperty('voices')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # Select the first voice in the list

# Convert text to speech
text = "Hello world! This is an example text-to-speech program."
engine.say(text)
engine.runAndWait()
