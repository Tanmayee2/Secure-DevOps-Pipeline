from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(status="UP"), 200

@app.route('/api')
def api():
    return jsonify(message="Hello from Secure DevOps Pipeline!")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
