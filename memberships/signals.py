from django.db.models.signals import post_save, post_delete
from django.conf import settings

from .models import UserMemebership, Membership

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def post_save_usermembership_create(sender, instance, created, *args, **kwargs):
    user_membership, created = UserMembership.objects.get_or_create(
        user=instance)

    if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id == '':
        new_customer_id = stripe.Customer.create(email=instance.email)
        free_membership = Membership.objects.get(membership_type='Free')
        user_membership.stripe_customer_id = new_customer_id['id']
        user_membership.membership = free_membership
        user_membership.save()


post_save.connect(post_save_usermembership_create,
                  sender=settings.AUTH_USER_MODEL)
