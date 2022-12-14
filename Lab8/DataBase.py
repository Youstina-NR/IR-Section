# cmd :
# pip install flask-sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	email= db.Column(db.String(80),unique=True,nullable=False)
	image_file = db.Column(db.String(20),default='default.jpg',nullable=False)
	password = db.Column(db.String(60),nullable=False)
	posts = db.relationship('Post',backref='author',lazy=True)
	
	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(100),nullable=False)
	date_posted= db.Column(db.DateTime,nullable=False,default=datetime.utcnow())
	content = db.Column(db.Text,nullable=False)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
	
	def __repr__(self):
		return f"Post('{self.title}','{self.date_posted}')"

