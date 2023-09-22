from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LessonViewSet, ProductViewSet

router_v1 = DefaultRouter()
router_v1.register('lessons', LessonViewSet, basename='lessons')
router_v1.register('statistic', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router_v1.urls)),
]
