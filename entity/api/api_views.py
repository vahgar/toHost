from rest_framework.generics import ListAPIView
from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from entity.models import business_entity
from .serializers import EntitySerializer

class EntityListAPIView(ListAPIView):
    queryset = business_entity.objects.all()
    serializer_class = EntitySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAuthenticated]
