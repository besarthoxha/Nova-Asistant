from flask import Flask, send_file, request, jsonify, Response
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        key = os.environ.get('ANTHROPIC_KEY', '')
        data = request.json
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': key,
            'anthropic-version': '2023-06-01'
        }
        res = requests.post(
            'https://api.anthropic.com/v1/messages',
            json=data,
            headers=headers
        )
        return jsonify(res.json())
    except Exception as e:
        return jsonify({'error': {'message': str(e)}}), 500

@app.route('/speak', methods=['POST'])
def speak():
    try:
        el_key = os.environ.get('EL_KEY', '')
        data = request.json
        text = data.get('text', '')
        voice_id = 'cgSgspJ2msm6clMCkdW9'
        res = requests.post(
            f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}',
            headers={
                'Content-Type': 'application/json',
                'xi-api-key': el_key
            },
            json={
                'text': text,
                'model_id': 'eleven_multilingual_v2',
                'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75}
            }
        )
        return Response(res.content, mimetype='audio/mpeg')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
