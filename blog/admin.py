from django.contrib import admin

# Register your models here.
from .models import posts, contact
admin.site.register(posts)
admin.site.register(contact)
