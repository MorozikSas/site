from rest_framework.serializers import ModelSerializer

from store.models import Goods


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'
