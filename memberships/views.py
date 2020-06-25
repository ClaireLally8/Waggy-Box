from django.conf import settings
from django.shortcuts import render, redirect, reverse
from .models import Membership, UserMembership, Subscription
from django.contrib.auth.decorators import login_required

import stripe

stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY

@login_required()
def get_user_membership(request):
    current_user_qs = UserMembership.objects.filter(user=request.user)
    if current_user_qs.exists():
        return current_user_qs.first()
    return None

@login_required()
def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(
        user_membership=get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None

@login_required()
def get_selected_membership(request):
    membership_type = request.session['selected_membership_type']
    selected_membership_qs = Membership.objects.filter(
        membership_type=membership_type)
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None

@login_required()
def membership_list(request):
    if request.method == "POST":
        selected_membership_type = request.POST.get('membership_type')
        selected_membership = Membership.objects.get(
            membership_type=selected_membership_type)
        request.session['selected_membership_type'] = selected_membership.membership_type

        context = {

            'selected_membership': selected_membership,
            'stripe_public_key': stripe_public_key,
        }
        return render(request, 'memberships/payment.html', context)

    memberships = Membership.objects.all()
    current_membership = get_user_membership(request)
    user_membership = str(current_membership.membership)
    context = {
        'memberships': memberships,
        'user_membership': user_membership,
    }

    return render(request, 'memberships/membership_list.html', context)

@login_required()
def payments(request):
    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)

    if request.method == "POST":
        token = request.POST['stripeToken']
        customer = stripe.Customer.retrieve(user_membership.stripe_customer_id)
        customer.source = token
        customer.save()

        subscription = stripe.Subscription.create(
                customer=user_membership.stripe_customer_id,
                items=[
                    {"plan": selected_membership.stripe_plan_id},
                ]
            )
        subscription_id = subscription.id

        user_membership = get_user_membership(request)
        selected_membership = get_selected_membership(request)
        user_membership.membership = selected_membership
        user_membership.save()

        sub, created = Subscription.objects.get_or_create(
            user_membership=user_membership)
        sub.stripe_subscription_id = subscription_id
        sub.active = True
        sub.save()

        try:
            del request.session['selected_membership_type']
        except:
            pass

        return render(request, 'memberships/update-success.html')

    context = {
        'selected_membership': selected_membership
    }

    return render(request, 'memberships/payment.html', context)

def subscription_overview(request):
    user = get_user_membership(request)
    subscription = get_user_subscription(request)

    context = {
        'user': user,
        'subscription': subscription,
    }
    return render(request, memberships/subscription_overview.html, context)