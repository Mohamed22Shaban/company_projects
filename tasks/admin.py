from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(EmailSender)
admin.site.register(EmailSubscribe)
