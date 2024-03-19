from flask import Flask, Blueprint,render_template
from pybo.models import Question


bp = Blueprint("question",__name__,url_prefix="/question")

@bp.route("/detail/<int:question_id>")
def detail(question_id):
    question = Question.query.get(question_id)

    return render_template("question/question_detail.html",question=question)

@bp.route("/list")
def question():
    question_list = Question.query.order_by(Question.create_date.desc())
   
    return render_template("question/question_list.html",question_list=question_list)