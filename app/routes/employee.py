from app import db
from flask import request, redirect, render_template, Blueprint, url_for
from flask_login import login_required,current_user
from app.models import LeaveInfo
from datetime import date

employee = Blueprint('employee',__name__)

@employee.route('/dashboard')
@login_required
def User_dashboard():
    return ("<p>dashboard</p>")

@employee.route("/leave/apply", methods=['GET','POST'])
@login_required
def leaveForm():
    
    if request.method=="POST":
        
        Leave_type=request.form.get('leave_type')
        Start_date=date.fromisoformat(request.form.get('start_date'))
        End_Date=date.fromisoformat(request.form.get('end_date'))
        Leave_Reason=request.form.get('reason')
        status= 'pending'
        info=LeaveInfo(user_id=current_user.id, leave_type=Leave_type, start_date=Start_date, end_date=End_Date, reason=Leave_Reason, status=status)
        
        db.session.add(info)
        db.session.commit()
        
        return redirect(url_for("employee.User_dashboard"))
    else:
        return render_template("employee/leave_apply.html")
    
@employee.route("/leave/history")
@login_required
def Leave_history():
    leaves = LeaveInfo.query.filter_by(user_id=current_user.id).all()
    return render_template('employee/leave_history.html',leaves=leaves)