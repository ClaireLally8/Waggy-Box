from django.test import TestCase
from django.contrib.auth.models import User
from memberships.models import UserMembership, Membership, Subscription
from shop.models import CurrentItem
from checkout.forms import OrderForm

class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            email='testing@mail.com',
            username='supertestuser',
            password='supertestinguser123'
        )

        membership_type = Membership.objects.create(
            membership_type='Premium',
            price=3.99,
            description_one='',
            description_two='',
            description_three='',
            description_four='',
            stripe_plan_id='price_1GyL11LBUH62NJcIvTn7Zx0e'
        )

        Item = CurrentItem.objects.create(
            name='Test Product',
            description='Test Description',
            price=45.99,
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

    def test_get_checkout(self):
        user = self.client.login(
            username='supertestuser', password='supertestinguser123')
        membership = Membership.objects.get(user=user)
        response = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '8',
            'expiry_year': '2025',
            'stripe_id': 'tok_visa',
        })

        self.assertTrue(response.status_code, 200)


class CheckoutFormsTests(TestCase):

    def test_valid_payment_form(self):
        form = OrderForm({
            'full_name':"Testing User",
            'email':"testing@testingtest.com",
            'phone_number':'123456789',
            'town_or_city':"Fakevile",
            'street_address1':"123 fakeotwn",
            'county':"whatisthis"
        })

        self.assertTrue(form.is_valid())
