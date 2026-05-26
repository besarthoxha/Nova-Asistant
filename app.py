from flask import Flask, send_file, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
