from django.test import SimpleTestCase
from django.urls import reverse


class TestUrl(SimpleTestCase):
    def test_url_exist(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
