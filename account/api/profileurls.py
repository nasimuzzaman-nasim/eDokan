from django.urls import path
from account.api.views import profile_view  #Profile

urlpatterns = [
    path('', profile_view, name="profile")
]
