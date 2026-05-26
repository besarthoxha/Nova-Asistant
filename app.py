from flask import Flask, send_file
app = Flask(__name__)

@app.route('/')
def home():
    return send_file('Nova 2.0.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
