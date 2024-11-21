from django.contrib import admin
from .models import *

r = admin.site.register

r(Cliente)
