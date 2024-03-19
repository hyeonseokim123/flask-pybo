from flask import Flask,Blueprint,render_template

bp = Blueprint("test",__name__,url_prefix="/test")

@bp.route("/say")
def say():
    ls1 = ["a","b","c"]

    return render_template("test/say.html", ls1=ls1)

@bp.route("/login")
def login():
    return render_template("/test/login.html")