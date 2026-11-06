from datetime import date

from django.test import Client, TestCase
from django.urls import reverse

from .models import Rent


class DeleteRentTests(TestCase):
    def setUp(self):
        self.rent = Rent.objects.create(
            client_name='Test client',
            item='Test item',
            queantity=1,
            tel_number='123456789',
            return_date=date(2026, 1, 1),
        )
        self.delete_url = reverse('delete_rent', args=[self.rent.id])

    def test_rent_list_has_csrf_protected_delete_form(self):
        response = self.client.get(reverse('all_rents'))

        self.assertContains(response, f'action="{self.delete_url}"')
        self.assertContains(response, 'method="post"')
        self.assertContains(response, 'name="csrfmiddlewaretoken"')

    def test_post_deletes_rent_and_redirects_to_list(self):
        response = self.client.post(self.delete_url)

        self.assertRedirects(response, reverse('all_rents'))
        self.assertFalse(Rent.objects.filter(id=self.rent.id).exists())

    def test_post_without_csrf_token_does_not_delete_rent(self):
        client = Client(enforce_csrf_checks=True)

        response = client.post(self.delete_url)

        self.assertEqual(response.status_code, 403)
        self.assertTrue(Rent.objects.filter(id=self.rent.id).exists())

    def test_get_does_not_delete_rent(self):
        response = self.client.get(self.delete_url)

        self.assertEqual(response.status_code, 405)
        self.assertTrue(Rent.objects.filter(id=self.rent.id).exists())
