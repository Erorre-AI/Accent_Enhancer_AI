import langid
import openai
import os

openai.api_key = "Key"

def translation(text):
    language, _ = langid.classify(text)
    if language == "en":
        return text
    else:
        prompt = f"Translate the following text into English and return only translation nothing else.:\n\n{text}\n\nTranslation:"

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional Translator to English."},
                {"role": "user", "content": prompt}
            ]
        )

        Translation_response = response.choices[0].message.content
        return Translation_response
# Example Usage
print(translation("Hello, how are you?"))  # True
print(translation("Bonjour, comment ça va?"))  # False
print(translation("ایک ٹیلے پر واقع مزار خواجہ فریدالدین گنج شکرؒ کے احاطہء صحن میں ذرا سی ژالہ باری چاندی کے ڈھیروں کی مثل بڑے غضب کا نظارا دیتی ہے۔"))
