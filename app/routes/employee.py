from flask import Blueprint
from flask_login import login_required

employee = Blueprint('employee',__name__)

@employee.route('/dashboard')
@login_required
def User_dashboard():
    return ("<p>dashboard</p>")

