from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from base.views import index


class Testurls(SimpleTestCase):

    def test_index_urls(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

