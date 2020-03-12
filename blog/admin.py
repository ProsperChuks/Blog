from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(posts)
admin.site.register(contact)
admin.site.register(comment)
