from App import db, login_manager, app
from datetime import datetime, timezone
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self):
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        return serializer.dumps({'user_id' : self.id}, salt= app.config['SECURITY_PASSWORD_SALT'])
    
    @staticmethod
    def verify_reset_token(token, exp_time=300):
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        try:
            user_id = serializer.loads(token, max_age=exp_time, salt=app.config['SECURITY_PASSWORD_SALT'])['user_id']
        except:
            None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
        
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.now(timezone.utc))
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    message= db.Column(db.String(), nullable=False)