from flask import Blueprint, request, jsonify
import openai
from .models import SessionLocal
from .repositories import QuestionRepository
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

main = Blueprint('main', __name__)

@main.route('/ask', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt', None)

    if (prompt is None):
        return jsonify({"error": "Prompt is required"}), 400

    try:
        client = openai.OpenAI(api_key=openai.api_key)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )

        answer = response.choices[0].message.content.strip()

        session = SessionLocal()
        question_repo = QuestionRepository(session)
        question_repo.add_question(prompt, answer)

        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500