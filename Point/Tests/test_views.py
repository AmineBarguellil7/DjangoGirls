from django.test import TestCase,Client
from django.contrib.auth.models import User
from django.urls import reverse
from Point.models import Marker
import json




class TestViews(TestCase):


    def setUp(self):
        self.client=Client()
        self.ShowMap_url=reverse("ShowMap")
        self.Home_url=reverse('Home')


    def test_marker_list_get(self):
        user = User.objects.create_user(username='testuser', password='test')
        self.client.force_login(user)
        response=self.client.get(self.ShowMap_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, "Point/map.html")


    def test_marker_home(self):
        response=self.client.get(self.Home_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, "Point/Home.html")
    


