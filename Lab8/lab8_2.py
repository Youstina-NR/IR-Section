from DataBase import db,User, Post

print(User.query.all())
print(User.query.first())
print(User.query.filter_by(username='Ali').all())
print(User.query.filter_by(username='Ali').first())
user1 = User.query.filter_by(username='Ali').first()
print(user1.id)
print(user1.username)
print(user1.email)
print(user1.password)

db.session.delete(user1)
db.session.commit()
user1 = User.query.filter_by(username='Ali').first()
print(user1)

#Getting user by primary key:
user = User.query.get(1)
print(user)
print(user.posts)





post = Post.query.first()
print(post)
print(post.user_id)
print(post.author)
