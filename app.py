from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello Guys from DevOps Lab!</h1><p>Deployed via CI/CD</p>"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
