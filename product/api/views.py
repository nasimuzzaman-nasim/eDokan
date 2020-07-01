from rest_framework import status, viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.pagination import PageNumberPagination

from product.models import Product
from product.api.serializers import ProductSerializer, CustomerProductSerializer
from .permission import ReadOnly


class ProductViewSetAdmin(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [ReadOnly]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    


# @api_view(['GET'])
# @permission_classes([permissions.AllowAny])
# @pagination_class([PageNumberPagination])
# def product_view(request):
#     products = Product.objects.filter(approved=True)
#     serializer = CustomerProductSerializer(products, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

class ProductView(generics.ListAPIView):
    queryset = Product.objects.filter(approved=True)
    serializer_class = CustomerProductSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def product_detail_view(request, slug):
    try:
        product = Product.objects.get(slug=slug, approved=True)
    except Product.DoesNotExist:
        return Response({'response': 'Item doesn\'t exist!'}, status=status.HTTP_404_NOT_FOUND)

    
    serializer = CustomerProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

    