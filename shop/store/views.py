from rest_framework.viewsets import ModelViewSet
from store.models import Goods
from store.serializers import ProductSerializer


class GoodsViewSet(ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = ProductSerializer
