from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BrandViewSet

router = DefaultRouter()
router.register(r'brands', BrandViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
