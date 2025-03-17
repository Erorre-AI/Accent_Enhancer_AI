from flask import Flask, render_template, request, jsonify, send_file
import os
import tempfile

from dotenv import load_dotenv

from accent_enhancer.Functionalities import text_to_speech_elevenlabs, transcribe_audio, accent_change, translation

# Load environment variables from .env file if it exists
try:
    load_dotenv()
except:
    pass

app = Flask(__name__)


# Create a temporary directory for audio files
UPLOAD_FOLDER = tempfile.mkdtemp()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    """Process the uploaded audio file."""
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']

    # Save the file temporarily
    temp_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_audio.webm')
    audio_file.save(temp_path)

    try:
        # Process the audio
        original_text = transcribe_audio(temp_path)
        translated_text = translation(original_text)
        american_accent = accent_change(translated_text)

        # Return the texts for display
        return jsonify({
            'original_text': original_text,
            'enhanced_text': american_accent
        })
    except Exception as e:
        print(f"Error processing audio: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/get_audio', methods=['POST'])
def get_audio():
    """Generate and return the enhanced speech audio."""
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        audio_bytes = text_to_speech_elevenlabs(text)

        # Create temporary file for the audio
        temp_audio_path = os.path.join(app.config['UPLOAD_FOLDER'], 'enhanced_audio.mp3')
        with open(temp_audio_path, 'wb') as f:
            f.write(audio_bytes.getvalue())

        return send_file(
            temp_audio_path,
            mimetype='audio/mp3',
            as_attachment=True,
            download_name='enhanced_audio.mp3'
        )
    except Exception as e:
        print(f"Error generating audio: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Speech Accent Enhancer is running!")
    print("Access the application at http://localhost:5000")
    app.run(debug=True)