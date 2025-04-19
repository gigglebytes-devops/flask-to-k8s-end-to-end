from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Sample data
quotes = [
    {"author": "Albert Einstein", "quote": "Life is like riding a bicycle. To keep your balance you must keep moving."},
    {"author": "Isaac Newton", "quote": "If I have seen further it is by standing on the shoulders of Giants."},
    {"author": "Yoda", "quote": "Do or do not. There is no try."}
]

jokes = [
    {"setup": "Why did the computer show up at work late?", "punchline": "It had a hard drive!"},
    {"setup": "Why do programmers prefer dark mode?", "punchline": "Because light attracts bugs!"},
    {"setup": "Why was the math book sad?", "punchline": "Because it had too many problems."}
]

@app.route('/')
def home():
    return "Welcome to the Simple Flask API!"

@app.route('/api/quote', methods=['GET'])
def get_quote():
    return jsonify(random.choice(quotes))

@app.route('/api/joke', methods=['GET'])
def get_joke():
    return jsonify(random.choice(jokes))

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
