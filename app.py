from flask import Flask, render_template
#from flask_security import SQLAlchemyDatastore, Security
#from flask_admin import Admin

#from core.models import db
#from auth.models import User, Role
#from auth.helpers import init_security


#security = Security()
app = Flask(__name__)
#admin = Admin(base_template='admin/master.html', template_mode='bootstrap3')
#from core import core as core_blueprint
#app.register_blueprint(core_blueprint)
#from auth import auth as auth_blueprint
#app.register_blueprint(auth_blueprint)

@app.route('/')
def index():
    return render_template('modular.html', raised=True)
