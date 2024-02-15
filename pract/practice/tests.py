from rest_framework.test import APITestCase
from django.urls import reverse
from .models import UserDetails

class UserViewTestCase(APITestCase):
    def setUp(self):
        self.user = UserDetails.objects.create(name="John Doe", age=30)

    def test_get_user_detail(self):
        url = reverse('user_detail', kwargs={'id': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['user']['name'], 'John Doe')
        self.assertEqual(response.data['user']['age'], 30)
        self.assertEqual(response.data['user']['id'], self.user.id)

    def test_create_user(self):
        url = reverse('user_list')
        data = {'name': 'Jane Smith', 'age': 25}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserDetails.objects.count(), 2)

    def test_update_user(self):
        url = reverse('user_detail', kwargs={'id': self.user.id})
        data = {'name': 'Jane Doe', 'age': 35}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, 'Jane Doe')
        self.assertEqual(self.user.age, 35)

    def test_partial_update_user(self):
        url = reverse('user_detail', kwargs={'id': self.user.id})
        data = {'age': 40}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.age, 40)

    def test_delete_user(self):
        url = reverse('user_detail', kwargs={'id': self.user.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(UserDetails.objects.filter(id=self.user.id).exists())
