from django.db import models

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
