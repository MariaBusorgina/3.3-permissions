from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AdvertisementFilter

