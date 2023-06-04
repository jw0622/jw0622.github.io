from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API 설정
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        message = request.form['message']

        response = openai.Completion.create(
            engine='davinci',
            prompt=message,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7
        )

        return jsonify({'message': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run()

