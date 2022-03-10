from flask import Flask
from job import jobs_api
from data import db_session

app = Flask(__name__)
app.register_blueprint(jobs_api)

db_session.global_init('db/db.sqlite')


@app.route('/')
def index():
    return 'Главная страница'

app.run()
