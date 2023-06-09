import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

GPT_API_URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'
GPT_API_KEY = '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'  # Replace with your actual GPT API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask():
    question = request.json['question']

    # Make API request to GPT API
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {GPT_API_KEY}'
    }
    data = {
        'prompt': question,
        'max_tokens': 50  # Adjust the desired length of the answer
    }
    response = requests.post(GPT_API_URL, headers=headers, json=data)
    answer = response.json()['choices'][0]['text'].strip() if response.ok else 'Sorry, I could not generate an answer.'

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run()

