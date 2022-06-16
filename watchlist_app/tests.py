from re import A
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status

from watchlist_app.api import serializers
from watchlist_app import models


class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='password123')
        self.token = Token.objects.get(user__username = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = 'Token '+ self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name="netflix",about= "something",website= "http://www.netflix.com")
        
    def test_stream_platform_create(self):
        data = {
            "name": "netflix",
            "about": "something",
            "website": "http://www.netflix.com"
        }    
        response = self.client.post(reverse('stream-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_stream_platform_list(self):
        response = self.client.get(reverse('stream-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
    def test_stream_platform_ind(self):    
        response = self.client.get(reverse('stream-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        
        
class WatchListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='password123')
        self.token = Token.objects.get(user__username = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = 'Token '+ self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name="netflix",about= "something",website= "http://www.netflix.com")
        self.watch = models.WatchList.objects.create(title="movie", storyline="story", platform = self.stream, active=True)
        
    def test_watchlist_create( self):
        data = {
            "title": "movie",
            "storyline": "story",
            "platform": self.stream,
            "active": True
        }
        response = self.client.post(reverse('watch-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_watchlist_list(self):    
        response = self.client.get(reverse('watch-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_watchlist_ind(self):    
        response = self.client.get(reverse('watch-detail', args=(self.watch.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
            
            
class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='password123')
        self.token = Token.objects.get(user__username = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = 'Token '+ self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name="netflix",about= "something",website= "http://www.netflix.com")
        self.watch = models.WatchList.objects.create(title="movie", storyline="story", platform = self.stream, active=True)
        
    def test_review_create(self):
        data = {
            "rating": 5,
            "watchlist": self.watch,
            "description": "something",
            "active": True
        }    
        response = self.client.post(reverse('review-create', args=(self.watch.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
                    
    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watch.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
                
            