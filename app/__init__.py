from flask import Flask
from app.database import mongo
from app.routes import todo_bp as todo
import os

def create_app():

    MONGO_CONNECTION_URI = os.environ.get(
        "MONGO_URL",
        "mongodb://localhost:27017/todo_db"
    )

    app = Flask(__name__)

    ''' MongoDB Configuration '''
    app.config['MONGO_URI'] = MONGO_CONNECTION_URI

    '''Initialize MongoDB '''
    # pymango.init_app(app) or 
    mongo.init_app(app)

    '''Register Blueprint'''
    app.register_blueprint(todo, url_prefix='/api')


    @app.route("/")
    def hello_world():
        return "<p>WELCOME, Todo App Reminder</p>"

    return app
    