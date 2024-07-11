from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Database setup
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Define the Question table
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)

# Create the tables in the database
Base.metadata.create_all(engine)

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

        answer = response.choices[0].message.content.strip()
        
        # Save the question and answer to the database
        session = Session()
        question_record = Question(question=prompt, answer=answer)
        session.add(question_record)
        session.commit()

        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
