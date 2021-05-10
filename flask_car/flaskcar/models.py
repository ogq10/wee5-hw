from datetime import datetime
from flaskcar import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = False)
    image_file = db.Column(db.String(20), nullable= False, default='default.png')
    posts = db.relationship('Post', backref='owner', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    car_name = db.Column(db.String(100), nullable= False)
    car_num = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)

    def __repr__(self):
        return f"Your Car:('{self.car_name}', '{car_num}', '{self.date_created}')"