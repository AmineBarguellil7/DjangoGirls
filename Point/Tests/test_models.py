from django.test import TestCase
from Point.models import Marker
from django.contrib.gis.geos import Point



class TestModels(TestCase):
    def setUp(self):
        self.marker= Marker.objects.create(name="New Marker", location=Point(1.2345, 2.3456))

    def test_marker_str(self):
        self.assertEqual(str(self.marker), "New Marker")

    def test_marker_location(self):
        self.assertEqual(self.marker.location.x, 1.2345)
        self.assertEqual(self.marker.location.y, 2.3456)    
