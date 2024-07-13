from flask import Flask
from .models import Base, engine
from .routes import main
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)

    load_dotenv()
    app.config['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

    # הגדרת מסד הנתונים
    Base.metadata.create_all(engine)

    # רישום נקודות הקצה
    app.register_blueprint(main)

    return app