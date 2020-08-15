from projectFiles import db
from datetime import datetime
from projectFiles import login_manager, UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from config import Config


# the db class
@login_manager.user_loader
def laod_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tabel__ = "User"
    __searchable__ = ['name', 'phoneNumber']  # these fields will be indexed by whoosh
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    userName = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    phoneNumber = db.Column(db.Integer(), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    proFimage = db.Column(db.String(50), nullable=False)
    proLink = db.Column(db.String(250), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, default=datetime.now())
    posts = db.relationship('Post', backref='person', lazy=True)


    # function 
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(Config.SECRET_KEY, expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(Config.SECRET_KEY)
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


class Post(db.Model):
    __tabel__ = "Post"
    __searchable__ = ['content']  # these fields will be indexed by whoosh
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())
    proFimage = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)




class Vister(db.Model):
    __tabel__ = "Vister"
    __searchable__ = ['content']  # these fields will be indexed by whoosh
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100), nullable=False)