import openai

openai.api_key = "Key"

def generate_speech(text, filename="output.mp3"):
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",  # Try 'nova', 'shimmer', 'echo' for variations
        input=text
    )

    with open(filename, "wb") as f:
        f.write(response.content)

    print("Speech generated successfully.")

# Example usage
text = "I am going to the store to buy some water."
generate_speech(text)