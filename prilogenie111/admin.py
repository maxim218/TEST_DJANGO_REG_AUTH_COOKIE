from django.contrib import admin
from .models import Town
from .models import Country

admin.site.register(Town)
admin.site.register(Country)