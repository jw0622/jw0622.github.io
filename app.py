from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask():
    question = request.json['question']

    # Make a request to the GPT API
    response = requests.post(
        'https://api.openai.com/v1/engines/davinci-codex/completions',
        headers={
            'Authorization': 'Bearer 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',
            'Content-Type': 'application/json',
        },
        json={
            'prompt': question,
            'max_tokens': 100,
        }
    )

    # Extract the answer from the GPT API response
    answer = response.json()['choices'][0]['text'].strip()

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run()
