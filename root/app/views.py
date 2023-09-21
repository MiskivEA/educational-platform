from rest_framework.response import Response
from rest_framework import viewsets

from .models import Product, Lesson, LessonView
from .serializers import LessonSerializer


class LessonViewSet(viewsets.ModelViewSet):

    serializer_class = LessonSerializer

    def get_queryset(self):
        my_products = self.request.user.access_products.all()




