from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy        #

import config

db = SQLAlchemy() # db객체
migrate = Migrate()


def create_app():

    app = Flask(__name__)
    app.config.from_object(config) # app에 config 등록

    db.init_app(app) #환경설정파일 초기화

    migrate.init_app(app, db)

    from . import models

    from .views import main_views,test_views,question_views,answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(test_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app
