from django.contrib import admin
from account.models import UserProfile, BaseAccount


admin.site.register(BaseAccount)
admin.site.register(UserProfile)