from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


db = SQLAlchemy()



class Student(db.Model, UserMixin):
    __name__ = "Students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name=db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True)
    level=db.Column(db.String(255))
    hostel=db.Column(db.String(255))
    special_circumstances=db.Column(db.String(255))
    profile_picture = db.Column(db.String(255))
    guardian=db.Column(db.String(255))
    ###Medical
    physician_name=db.Column(db.String(255))
    physician_no = db.Column(db.String(255))
    insurance_carrier = db.Column(db.String(255))    
    profile_picture = db.Column(db.String(255))
    insurance_no=db.Column(db.String(255))
    medication=db.Column(db.String(255))
    ##guardian
    name = db.Column(db.String(255))
    relationship = db.Column(db.String(255))
    email = db.Column(db.String(255))
    bussiness_No= db.Column(db.String(255))
    home_No= db.Column(db.String(255))
    mobile_no= db.Column(db.String(255))
    emergency= db.Column(db.String(255))

"""

class Guardian(db.Model, UserMixin):
    __name__ = "Guardian"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    relationship = db.Column(db.String(255))
    email = db.Column(db.String(255))
    bussiness_No= db.Column(db.String(255))
    home_No= db.Column(db.String(255))
    mobile_no= db.Column(db.String(255))
    emergency= db.Column(db.String(255))
"""
    