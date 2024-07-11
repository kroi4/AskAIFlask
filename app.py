from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/ask', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt', '')

    try:
        client = openai.OpenAI(api_key=openai.api_key)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )

        return jsonify({"response": response.choices[0].message.content.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
