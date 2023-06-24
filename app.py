from flask import Flask, jsonify, request, g
from flask_sqlalchemy import SQLAlchemy
#create the db instance in extensions file so that blog_repo and blog service and import from there
#rather than importing from this app.py file causing circular import issue
from extensions import db
from models import Post, User
from blog_repository import BlogRepository
from blog_service import BlogService



app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # SQLite database URI
db.init_app(app)

#create a blog_repository instance
blog_repository = BlogRepository()

#create a blog_service instance
blog_service = BlogService(blog_repository)

#define the endpoints
@app.route('/', methods=['GET'])
def home():
    return "Welcome to Seewah's Blog API"

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = blog_service.get_all_posts()
    return jsonify(posts)

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = blog_service.get_post_by_id(post_id)
    if post:
        return jsonify(post)
    return jsonify({'message': 'Post not found'}), 404

@app.route('/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Invalid data'}), 400

    # blog_service.initialize()

    post = blog_service.create_post(data)
    return jsonify(post), 201

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Invalid data'}), 400
    post = blog_service.update_post(post_id, data)
    if post:
        return jsonify(post)
    return jsonify({'message': 'Post not found'}), 404

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def remove_post(post_id):
    success = blog_service.delete_post(post_id)
    if success:
        return jsonify({'message': 'Post deleted'})
    return jsonify({'message': 'Post not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

#hi
