from datetime import datetime
from flask import g


class BlogService:

    def __init__(self, blog_repository):
        self.blog_repository = blog_repository

    # def initialize(self):
    #     self.blog_repository = BlogRepository()

    def get_all_posts(self):
        # blog_repository = g.get('blog_repository')
        posts = self.blog_repository.get_all_posts()
        serialized_posts = [
            {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'user_id': post.user_id
            }
            for post in posts
        ]
        return serialized_posts

    def get_post_by_id(self, post_id):
        blog_repository = self.blog_repository
        post = blog_repository.get_post_by_id(post_id)
        serialized_post = [
            {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'user_id': post.user_id
            }
        ]
        return serialized_post

    def create_post(self, data):
        blog_repository = self.blog_repository
        post_data = {
            'title': data['title'],
            'content': data['content'],
            'user_id': data['user_id'],
            'created_at': datetime.utcnow()
        }
        post = blog_repository.create_post(post_data)

        post_dict = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            # Add other fields if needed
        }

        return post_dict


    def update_post(self, post_id, data):
        blog_repository = self.blog_repository
        return blog_repository.update_post(post_id, data)

    def delete_post(self, post_id):
        blog_repository = self.blog_repository
        return blog_repository.delete_post(post_id)
