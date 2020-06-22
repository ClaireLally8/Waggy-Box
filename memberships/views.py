from django.conf import settings
from django.shortcuts import render
from .models import Membership, UserMembership, Subscription


def get_user_membership(request):
    current_user_qs = UserMembership.objects.filter(user=request.user)
    if current_user_qs.exists():
        return current_user_qs.first()
    return None


def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(user_membership=get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


def membership_list(request):
    memberships = Membership.objects.all()
    current_membership = get_user_membership(request)
    user_membership = str(current_membership.membership)
    context = {
        'memberships': memberships,
        'user_membership': user_membership,
    }

    return render(request, 'memberships/membership_list.html', context)


def selected_membership(request):
    if request.method == "POST":
        current_membership = get_user_membership(request)
        selected_membership_type = request.POST.get('membership_type')
        selected_membership = Membership.objects.get(membership_type=selected_membership_type)

        return render(request, 'memberships/payment.html')