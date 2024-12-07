from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "what is enigma e-cell": "Enigma E-Cell NMIT is an entrepreneurship cell aimed at fostering innovation and startup culture."
    # Add more predefined responses here
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message').lower()
    reply = responses.get(user_message, "I'm sorry, I didn't understand that.")
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)