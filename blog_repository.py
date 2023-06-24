from extensions import db
from models import User, Post

class BlogRepository:
    def get_all_posts(self):
        return Post.query.all()

    def get_post_by_id(self, post_id):
        return Post.query.get(post_id)

    def create_post(self, data):
        post = Post(title=data['title'],
                    content=data['content'],
                    user_id=data['user_id']
                    )
        # user = User.query.get(data['user_id'])
        # if user:
        #     post.author = user
        db.session.add(post)
        db.session.commit()
        return post

    def update_post(self, post_id, data):
        post = Post.query.get(post_id)
        if post:
            post.title = data.get('title', post.title)
            post.content = data.get('content', post.content)
            db.session.commit()
            return post
        return None

    def delete_post(self, post_id):
        post = Post.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return True
        return False
