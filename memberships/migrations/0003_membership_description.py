# Generated by Django 3.0.7 on 2020-06-21 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0002_remove_membership_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]