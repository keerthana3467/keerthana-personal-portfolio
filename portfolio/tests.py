from django.test import TestCase
from django.urls import reverse
from .models import ContactMessage

class PortfolioPageTests(TestCase):
    def test_home_page_loads(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Keerthana')
        self.assertContains(response,'Fitness Tracking System')
        self.assertContains(response,'Blog Platform')
    def test_project_detail_pages_load(self):
        for slug in ['fitness-tracking-system','blog-platform']:
            with self.subTest(slug=slug):
                self.assertEqual(self.client.get(reverse('project_detail',args=[slug])).status_code,200)
    def test_invalid_project_returns_404(self):
        self.assertEqual(self.client.get('/projects/does-not-exist/').status_code,404)
    def test_contact_form_stores_message_email_optional(self):
        response=self.client.post(reverse('home'),{'name':'Test Visitor','email':'','subject':'Hello','message':'Portfolio contact test'})
        self.assertRedirects(response,reverse('home'))
        self.assertEqual(ContactMessage.objects.count(),1)
        self.assertEqual(ContactMessage.objects.first().email,'')
    def test_contact_form_rejects_invalid_email(self):
        response=self.client.post(reverse('home'),{'name':'Test Visitor','email':'invalid','subject':'Hello','message':'Check email validation'})
        self.assertEqual(response.status_code,200)
        self.assertEqual(ContactMessage.objects.count(),0)
