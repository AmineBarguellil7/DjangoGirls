from django.test import SimpleTestCase
from django.urls import reverse,resolve
from Point.views import ShowMap,save_marker


class TestUrls(SimpleTestCase):
    def test_ShowMap_url_is_resolved(self):
        url=reverse('ShowMap')
        self.assertEquals(resolve(url).func,ShowMap)

    def test_save_marker_url_is_resolved(self):
        url=reverse('save_marker')
        self.assertEquals(resolve(url).func,save_marker)