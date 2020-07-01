from rest_framework.routers import DefaultRouter
from product.api.views import ProductViewSetAdmin #, ProductViewSetCustomer


router = DefaultRouter()
router.register(r'admin/products', ProductViewSetAdmin)
# router.register(r'products', ProductViewSetCustomer)
urlpatterns = router.urls

# , basename='product'