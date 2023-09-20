from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'app'

router_v1 = DefaultRouter()
router_v1.register(r'available-lessons', LessonViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
]