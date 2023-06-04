import openai

app = Flask(__name__)

# OpenAI API 설정
openai.api_key = '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'

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']

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
