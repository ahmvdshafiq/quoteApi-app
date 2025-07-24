from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

# Load quotes from a file
with open("quotes.json") as f:
    quotes = json.load(f)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Quote API!"})

@app.route('/quote')
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
