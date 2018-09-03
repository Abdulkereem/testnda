from flask import Flask 
from flask import Flask 
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy.exc import *
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_pyfile('config.py')

from dashboard.admin.model import *
from dashboard.admin.view import index
db.init_app(app)

administrator = Admin(app, name='Control Panel')
administrator.add_view(ModelView(Student, db.session))
#administrator.add_view(ModelView(Guardian,db.session))


app.register_blueprint(admin.view.index)


