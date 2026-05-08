from flask import Blueprint,request, redirect, url_for,render_template
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from app import db
from app.models import UserInfo

auth = Blueprint('auth',__name__)

@auth.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email = request.form.get("email")    
        password = request.form.get("password")
        user=UserInfo.query.filter_by(email=email).first()
        if user is None:
            return render_template('auth/login.html', error= "User doesnt Exist")
        else: 
            check_password=check_password_hash(user.password_hash,password)
        
        if user and check_password:
            login_user(user)
            return redirect(url_for('employee.User_dashboard'))
        else :
            return render_template("auth/login.html", error = "invalid email or password")
    else: 
        return render_template("auth/login.html")


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/register", methods=['GET','POST'])
def register():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        role = "employee"
        hashed=generate_password_hash(password)
        user = UserInfo (name=name, email=email, password_hash=hashed, role=role)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    else : 
        return render_template("auth/register.html")

