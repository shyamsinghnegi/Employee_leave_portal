from app import db,login_manager
from flask_login import UserMixin

class UserInfo(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    role = db.Column(db.String(20))
    password_hash = db.Column(db.String(256))
        
@login_manager.user_loader
def load_user(user_id):
    return UserInfo.query.get(int(user_id))
    
class LeaveInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    leave_type = db.Column(db.String(50))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(20))
    reason = db.Column(db.String(300))
    
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    manager_id = db.Column(db.Integer, db.ForeignKey('user_info.id')) 