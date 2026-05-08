from flask import request,render_template

from app import create_app

app=create_app()

@app.route("/")
def Firstflaskfunc():
    return ("<p>First flask function</p>")

    