# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import models

# Create your views here.
def index(request):
    return render(request,
                  'index/index.html')