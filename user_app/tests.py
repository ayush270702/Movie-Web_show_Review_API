from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status


class RegisterTestCase(APITestCase):
    def test_register(self):
        
        data = {
            "username": "testcase1",
            "email": "testcase@abc.com",
            "password": "testcase69",
            "password2":"testcase69"
        }
        
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
class LoginLogoutTestTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="password123")
        
    def test_login(self):
        data = {
            "username": "example",
            "password": "password123"
            }            
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_logout(self):
        self.token = Token.objects.get(user__username='example')
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)    




