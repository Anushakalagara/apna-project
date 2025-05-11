from flask import Flask, render_template, request, jsonify
from voice.mock_stt import transcribe_audio

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/voice", methods=["POST"])
def handle_voice():
    # Simulated response from a voice command
    user_text = request.json.get("text")
    response = "Your balance is ₹5000" if "balance" in user_text.lower() else "Command not recognized."
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)