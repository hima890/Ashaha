# import all the packigs
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_moment import Moment
from flask_mail import Mail, Message
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user
from config import Config
import atexit
# from flask_whooshalchemy import whoosh


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
moment = Moment()
mail = Mail()
# whoosh = whoosh()
login_manager = LoginManager()
login_manager.login_view = "loginLogout.login"
login_manager.login_message = "الشغل ما فوضى يا اصلي، سجل دخولك اول"
login_manager.login_message_category = "danger"

#the main app function
def create_app(config_class=Config):
    # the Flask class instaince 
    app = Flask(__name__)
    # import the configration from config file
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # whoosh.init_app(app)
    # create the database
    with app.app_context():
        import models
        db.create_all()
    # register the main blueprint
    from projectFiles.home.routes import home_page
    from projectFiles.loginLogout.routes import loginLogout_page
    from projectFiles.accounts.routes import account_page
    from projectFiles.resetPassword.rouets import reset_page
    from projectFiles.errors.routes import errors
    from projectFiles.admin.rouets import admin_page
    app.register_blueprint(home_page)
    app.register_blueprint(loginLogout_page)
    app.register_blueprint(account_page)
    app.register_blueprint(reset_page)
    app.register_blueprint(errors)
    app.register_blueprint(admin_page)
    return app
