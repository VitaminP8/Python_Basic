from django.test import TestCase
from .models import Category, Goal, User
from userapp.models import MyUser


class TestViews(TestCase):

    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        user = User.objects.create(name='user', surname='userovich')
        response = self.client.get('/')
        # print(response.context)
        self.assertTrue('users' in response.context)
        self.assertEqual(response.context['users'].first().id, user.id)

    def test_content(self):
        response = self.client.get('/')
        button_element = '<button class="btn btn-outline-success" type="submit">Search</button>'

        self.assertIn(button_element, response.content.decode(encoding='utf-8'))
        self.assertIn(button_element.encode(encoding='utf-8'), response.content)

    def test_category_list_auth(self):
        response = self.client.get('/category-list/')
        self.assertEqual(response.status_code, 302)

        username = 'auth_user'
        password = 'user123456'
        user = MyUser.objects.create_user(
            username='auth_user',
            email='user@user.com',
            password='user123456',
        )

        self.client.login(username=username, password=password)

        response = self.client.get('/category-list/')

        self.assertEqual(response.status_code, 200)

        self.client.logout()

        response = self.client.get('/category-list/')
        self.assertEqual(response.status_code, 302)
