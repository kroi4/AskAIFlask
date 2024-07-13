# app/repositories.py
from sqlalchemy.orm import Session
from .models import Question

class QuestionRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_question(self, question_text: str, answer_text: str):
        question = Question(question=question_text, answer=answer_text)
        self.session.add(question)
        self.session.commit()
        return question

    def get_question_by_id(self, question_id: int):
        return self.session.query(Question).filter(Question.id == question_id).first()