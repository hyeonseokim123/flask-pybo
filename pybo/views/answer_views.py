from flask import Flask,Blueprint,render_template,request,url_for
from pybo.models import Answer,Question
from datetime import datetime # 모듈안에 객체가 하나있다
from pybo import db
from werkzeug.utils import redirect


bp = Blueprint("answer",__name__,url_prefix="/answer")

@bp.route("/create/<int:question_id>", methods=('post', ))
def create(question_id):
    
    question = Question.query.get_or_404(question_id)

    content = request.form['content'] #form태그에서 보내준 데이터를 request에 저장 spring request flask안에 들어있다
    create_date = datetime.now()

    answer = Answer(question=question, contnet=content, create_date=create_date)
    db.session.add(answer)
    db.session.commit()

    return redirect(url_for("question.detail",question_id=question_id))