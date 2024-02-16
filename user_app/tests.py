from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegisterTestCase(APITestCase):
    
    def test_register(self):
        data = {
            'username' : 'ammar',
            'password' : 'password',
            'password2': 'password',
            'email'    : 'ammar@gmail.com'
        }
        
        response = self.client.post(reverse('register'),data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

class TestLoginLogout(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='ammar', password='password')
    
    def test_login(self):
        data = {
            'username' : 'ammar',
            'password' : 'password'
        }
        
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def test_logout(self):
        self.token = Token.objects.get(user__username='ammar')
        # set up token in the client ( client is like post will caryy headers)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        #  client is the postman
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)