from django.contrib import admin

# Register your models here.
from home.models import Contact,NewsLatter

admin.site.register(Contact)
admin.site.register(NewsLatter)