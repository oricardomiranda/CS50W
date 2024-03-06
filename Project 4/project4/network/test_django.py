from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import User, Post, Follower, Like

class MyTests(TestCase):

    def test_user_and_post_creation(self):
        # Create a user and a post
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(user=self.user, message='Test message')

    def test_index_page(self):
        self.test_user_and_post_creation()
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test message')


class MyViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(user=self.user, message='Test message')

    def test_new_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('new_post'), {'message': 'New test message'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)

    def test_add_like_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_like', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Like.objects.count(), 1)

    def test_remove_like_view(self):
        Like.objects.create(user=self.user, post=self.post)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('remove_like', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Like.objects.count(), 0)

    def test_follow_view(self):
        user_to_follow = get_user_model().objects.create_user(username='user_to_follow', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('follow'), {'userfollow': user_to_follow.username})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Follower.objects.count(), 1)

    def test_unfollow_view(self):
        user_to_unfollow = get_user_model().objects.create_user(username='user_to_unfollow', password='testpassword')
        Follower.objects.create(user=self.user, follower=user_to_unfollow)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('unfollow'), {'userfollow': user_to_unfollow.username})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Follower.objects.count(), 0)
