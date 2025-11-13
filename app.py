from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Render! 🚀"

@app.route('/test')
def test():
    return "Hello from Flask on Render test! 🚀"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
