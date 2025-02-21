# 1）Backend
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "XXXXXX"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message')

    # Send the input to ChatGPT API
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # Use the appropriate model
        messages=[{"role": "user", "content": user_input}]
    )

    # Extract the chatbot's response
    chatbot_reply = response['choices'][0]['message']['content']
    return jsonify({"response": chatbot_reply})

#if __name__ == '__main__':
#    app.run(debug=True)
