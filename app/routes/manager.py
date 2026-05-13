from app import db
from flask import request, redirect , render_template, Blueprint, url_for
from flask_login import login_required, current_user
from app.models import LeaveInfo

manager = Blueprint('manager', __name__)

@manager.route('/leaves')
@login_required
def Leave_Status():
    leaveinfo=LeaveInfo.query.filter_by(status='pending').all()
    return render_template('manager/leave_status.html',leaves=leaveinfo)


@manager.route('/approve_leave/<int:leave_id>')
@login_required
def approve_leave(leave_id):
    leave=LeaveInfo.query.get(leave_id)
    leave.status='approved'
    db.session.commit()
    return redirect(url_for('manager.Leave_Status'))

@manager.route('/reject_leave/<int:leave_id>')
@login_required
def reject_leave(leave_id):
    leave=LeaveInfo.query.get(leave_id)
    leave=status = 'rejected'
    db.session.commit()
    return redirect(url_for('manager.Leave_Status'))