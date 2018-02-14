from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils import timezone

import models
import forms

# Create your views here.
def index(request):
    return render(request,
                  'index/index.html')

def context_processor(request):
    site_user = request.user

    context = {
        'site_user': site_user,
    }

    return context

def user_dashboard(request, user_id):
    user_pro = models.UserProfile.objects.get(pk=user_id)
    today = timezone.now()
    events = models.NewEvent.objects.filter(host=user_pro, date_end__gte=today)

    context = {
        'user_pro': user_pro,
        'events': events,
    }

    return render(request,
                  'dashboard/index.html',
                  context)

def create_event(request, user_id):
    user_pro = models.UserProfile.objects.get(pk=user_id)

    context = {
        'user_pro': user_pro,
        'new_event_form': forms.NewEventForm(),
    }
    return render(request,
                  'dashboard/new_event.html',
                  context)
