from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import LessonViewSet

router_v1 = DefaultRouter()
router_v1.register('lessons/', LessonViewSet, basename='lessons')

urlpatterns = [
    path('', include(router_v1.urls)),
]
