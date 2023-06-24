import unittest
from datetime import datetime
from blog_service import BlogService


class BlogServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.blog_service = BlogService()

    def test_get_all_posts(self):
        posts = self.blog_service.get_all_posts()
        self.assertEqual(len(posts), 2)

    def test_get_post_by_id_existing(self):
        post = self.blog_service.get_post_by_id(1)
        self.assertIsNotNone(post)
        self.assertEqual(post['title'], 'First Post')

    def test_get_post_by_id_nonexistent(self):
        post = self.blog_service.get_post_by_id(3)
        self.assertIsNone(post)

    def test_create_post(self):
        data = {
            'title': 'New Post',
            'content': 'This is a new blog post.',
            'author': 'John Smith'
        }
        post = self.blog_service.create_post(data)
        self.assertIsNotNone(post)
        self.assertEqual(post['title'], 'New Post')
        self.assertEqual(post['content'], 'This is a new blog post.')
        self.assertEqual(post['author'], 'John Smith')
        self.assertEqual(post['id'], 3)
        self.assertIsInstance(post['created_at'], datetime)

    def test_update_post_existing(self):
        post_id = 1
        data = {
            'title': 'Updated Post',
            'content': 'This post has been updated.',
            'author': 'Jane Doe'
        }
        updated_post = self.blog_service.update_post(post_id, data)
        self.assertIsNotNone(updated_post)
        self.assertEqual(updated_post['title'], 'Updated Post')
        self.assertEqual(updated_post['content'], 'This post has been updated.')
        self.assertEqual(updated_post['author'], 'Jane Doe')
        self.assertEqual(updated_post['id'], 1)

    def test_update_post_nonexistent(self):
        post_id = 3
        data = {
            'title': 'Updated Post',
            'content': 'This post has been updated.',
            'author': 'Jane Doe'
        }
        updated_post = self.blog_service.update_post(post_id, data)
        self.assertIsNone(updated_post)

    def test_delete_post_existing(self):
        post_id = 2
        result = self.blog_service.delete_post(post_id)
        self.assertTrue(result)
        posts = self.blog_service.get_all_posts()
        self.assertEqual(len(posts), 1)

    def test_delete_post_nonexistent(self):
        post_id = 3
        result = self.blog_service.delete_post(post_id)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
