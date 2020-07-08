from django.test import TestCase
from django.contrib.auth.models import User
from memberships.models import UserMembership, Membership, Subscription
from django.conf import settings


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            email='testing@mail.com',
            username='supertestuser',
            password='supertestinguser123'
        )

        membership_type = Membership.objects.create(
            membership_type='free',
            price=3.99,
            description_one='',
            description_two='',
            description_three='',
            description_four='',
            stripe_plan_id='price_1GyL11LBUH62NJcIvTn7Zx0e'
        )

        membership = UserMembership.objects.create(
            user=user,
            stripe_customer_id='cus_12345667890',
            membership=membership_type,
            full_name="Testing User",
            email="testing@testingtest.com",
            phone_number='123456789',
            town_or_city="Fakevile",
            street_address1="123 fakeotwn",
            county="whatisthis"
        )

        subscription = Subscription.objects.create(
            user_membership=user,
            stripe_subscription_id='sub_12345667890',
            active=True
        )

    def test_get_landing_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_about_view(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about.html')

    def test_contact_view(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact.html')

    def test_dashboard_view(self):
        self.client.login(
            username='supertestuser', password='supertestinguser123')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'main/dashboard.html')
