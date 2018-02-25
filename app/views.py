from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseNotFound
from django.db.models import Prefetch

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
    guests = models.Guests.objects.filter(owner=user_id)

    context = {
        'user_pro': user_pro,
        'events': events,
        'guests': guests,
    }

    return render(request,
                  'dashboard/index.html',
                  context)

def user_contacts(request, user_id):
    user_pro = models.UserProfile.objects.prefetch_related('related_guest').get(pk=user_id)

    if request.is_ajax and 'new_guest' in request.POST:
        name = request.POST.get('guest_name')
        email = request.POST.get('guest_email')
        phone = request.POST.get('guest_phone')
        if email and name and phone:
            guest = models.Guests.objects.create(
                email=email,
                name=name,
                phone_number=phone,
                owner=user_pro,
            )
            guest.save()
            user_pro = models.UserProfile.objects.prefetch_related('related_guest').get(pk=user_id)
            return render(request,
                          'dashboard/guest_list.html',
                          {'user_pro': user_pro})

    context = {
        'user_pro': user_pro,
    }

    return render(request,
                  'dashboard/user_contacts.html',
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
            return HttpResponseRedirect('/profile/event/emails/{0}'.format(user_pro.id))
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

def event_emails(request, event_id):
    event = models.Event.objects.get(pk=event_id)
    print 'Guest count', event.get_guest_count()
    context = {
        'event': event
    }
    return render(request,
                  'event/emails.html',
                  context)

def event_edit(request, username, event_id):
    '''
    User edits their event here, can add guests to the guestlist as well to the the user's main guest list
    '''
    event = models.Event.objects.get(pk=event_id)
    user_pro = models.UserProfile.objects.prefetch_related('related_guest')\
                                            .get(username=username)

    if request.is_ajax and 'add_guest' in request.POST:
        name = request.POST.get('guest_name')
        email = request.POST.get('guest_email')
        phone = request.POST.get('guest_phone')
        new_guest = models.Guests.objects.create(
            name=name,
            email=email,
            phone_number=phone,
            owner=user_pro
        )
        new_guest.save()
        event.guests.add(new_guest)
        event.save()
        event = models.Event.objects.get(id=event_id)
        user_pro = models.UserProfile.objects.prefetch_related('related_guest')\
                                                .get(username=username)
        context = {
            'event': event,
            'user_pro': user_pro
        }
        return render(request,
                      'event/event_guests.html',
                      context)


    context = {
        'event': event,
        'user_pro': user_pro,
    }
    return render(request,
                  'event/edit.html',
                  context)

def event_page(request, username, event_id):
    event = models.Event.objects.get(id=event_id,
                                        host__username=username)

    context = {
        'event': event,
    }
    return render(request,
                  'event/index.html',
                  context)
