from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "✅ Herkules API Live!",
        "status": "READY"
    })

@app.route('/status')
def status():
    return jsonify({
        "system": "Herkules",
        "status": "ACTIVE",
        "minds": ["Mind1", "Mind2"],
        "performance": "75%"
    })

if __name__ == '__main__':
    print("🚀 API Running on http://localhost:5000")
    app.run(debug=True, port=5000)