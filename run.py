from flask import request,render_template

from app import create_app

app=create_app()

@app.route("/")
def Firstflaskfunc():
    return ("<p>First flask function</p>")

@app.route("/leave/apply", methods=['GET','POST'])
def leaveForm():
    if request.method=="POST":
        return ("<p>Form submitted !</p>")
    else:
        return render_template("leave_apply.html")
    