from django.contrib import admin
from django.contrib.sessions.models import Session

from .models import *

class imageAdmin(admin.ModelAdmin):
    list_display =["username", "pic"]

admin.site.register(Pictures, imageAdmin)
admin .site.register(Feedback)
admin.site.register(Session)
