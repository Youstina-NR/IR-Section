from DataBase import db,User, Post
db.drop_all()
db.create_all()

user_1 = User(username='Ahmed',email='ahmed@gmail.com',password='1234')
db.session.add(user_1)
user_2 = User(username='Ali',email='ali@gmail.com',password='1234')
db.session.add(user_2)
db.session.commit()


user = User.query.get(1)
post_1 = Post(title='p1',content='first post content!',user_id=user.id)
post_2 = Post(title='p2',content='second post content!',user_id=user.id)
db.session.add(post_1)
db.session.add(post_2)
db.session.commit()




