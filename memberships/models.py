from django.conf import settings
from django.db import models

import stripe

MEMBERSHIP_CHOICES = (
    ('Regular', 'reg'),
    ('Premium', 'prem'),
)


# Membership type View for DB admin
class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES,
        default='Regular',
        max_length=30)
    price = models.IntegerField(default=15)
    stripe_plan_id = models.CharField(max_length=40)

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(
        Membership, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


class Subscription(models.Model):
    user_membership = models.ForeignKey(
        UserMembership, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user_membership.user.username
