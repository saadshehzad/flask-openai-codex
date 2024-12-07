from flask import Flask, render_template, request, jsonify
import openai
from config import openai_api_key

openai.api_key = openai_api_key

app = Flask(__name__)

openai.api_key = 'your-openai-api-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_code', methods=['POST'])
def generate_code():
    user_prompt = request.form['prompt']
    
    if user_prompt:
        try:
            response = openai.completions.create(
                model="code-davinci-002",
                prompt=user_prompt,
                max_tokens=150,
                temperature=0.7
            )

            generated_code = response.choices[0].text.strip()

            return jsonify({'generated_code': generated_code})

        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'No prompt provided.'}), 400

if __name__ == '__main__':
    app.run(debug=True)