# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

import models

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
    pass
