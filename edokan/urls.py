from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include("account.api.urls")),
    path('api/profile/', include("account.api.profileurls")),
    path('api/', include("product.api.route")),
    path('api/products/', include("product.api.urls")),
]
