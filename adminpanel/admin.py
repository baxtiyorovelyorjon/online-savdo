from django.contrib import admin

# Register your models here.
from adminpanel.models import Client,Creater

admin.site.register(Client)
admin.site.register(Creater)