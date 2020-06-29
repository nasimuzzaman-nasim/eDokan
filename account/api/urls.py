from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from account.api import views as aav

app_name = 'auth'

urlpatterns = [
    path('register/', aav.registration_view, name="register"),
    path('login/', obtain_auth_token, name="login"),
    path('user-list/', aav.UserList.as_view(), name="user-list"),
    # path('profile/<str:username>/', aav.DetailView.as_view(), name="detail"),
]
