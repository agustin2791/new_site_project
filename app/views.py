from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseNotFound

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
    events = models.Event.objects.filter(host=user_pro, date_end__gte=today)

    context = {
        'user_pro': user_pro,
        'events': events,
    }

    return render(request,
                  'dashboard/index.html',
                  context)

def create_event(request, user_id):
    user_pro = models.UserProfile.objects.get(pk=user_id)
    initial = {
            'host': user_pro,
            'guests': None,
        }

    if request.method == 'POST' and 'new_event_save' in request.POST:
        new_event_form = forms.EventForm(request.POST)
        if new_event_form.is_valid():
            print 'it worked'
            saved_form = new_event_form.save()
            saved_form.save()
            new_event_form = forms.EventForm()
            return HttpResponseRedirect('/profile/{0}'.format(user_pro.id))
        else:
            print 'It did not work'
    else:
        new_event_form = forms.EventForm(initial=initial)

    context = {
        'user_pro': user_pro,
        'new_event_form': new_event_form,
    }
    return render(request,
                  'dashboard/new_event.html',
                  context)

def event_page(request, username, event_id):
    event = models.Event.objects.get(id=event_id,
                                        host__username=username)
    return HttpResponse('Yes!')
