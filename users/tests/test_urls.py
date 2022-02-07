from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from users.views import register


class Testurls(SimpleTestCase):

    def test_register_urls(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)