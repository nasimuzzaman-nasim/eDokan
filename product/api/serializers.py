from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:          
        model = Product
        fields = '__all__'  

        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CustomerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'