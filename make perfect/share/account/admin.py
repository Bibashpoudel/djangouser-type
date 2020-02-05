from django.contrib import admin

from .models import Idea, Sponsor ,Ideapeacher
from django.contrib.auth import get_user_model
User = get_user_model()

# Register your models here.
admin.site.register(User)
admin.site.register(Idea)
admin.site.register(Sponsor)
admin.site.register(Ideapeacher)