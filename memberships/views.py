from django.shortcuts import render
from .models import Membership, UserMembership, Subscription


def member_type(request):
    memberships = Membership.objects.all()
    context = {
        'memberships': memberships,
    }

    return render(request, 'memberships/membership_list.html', context)
