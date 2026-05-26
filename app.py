from flask import Flask, send_file, request, jsonify
import requests
import os

app = Flask(__name__)

ANTHROPIC_KEY = os.environ.get('ANTHROPIC_KEY', '')
EL_KEY = os.environ.get('EL_KEY', '')

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': ANTHROPIC_KEY,
        'anthropic-version': '2023-06-01'
    }
    res = requests.post('https://api.anthropic.com/v1/messages', 
                       json=data, headers=headers)
    return jsonify(res.json())

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    headers = {
        'Content-Type': 'application/json',
        'xi-api-key': EL_KEY
    }
    voice_id = data.get('voice_id', 'cgSgspJ2msm6clMCkdW9')
    res = requests.post(
        f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}',
        json=data, headers=headers
    )
    return res.content, 200, {'Content-Type': 'audio/mpeg'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
