from rest_framework.response import Response
from rest_framework import viewsets

from .models import Product, Lesson, LessonViewer
from .serializers import LessonSerializer


class LessonViewSet(viewsets.ModelViewSet):

    serializer_class = LessonSerializer

    def get_queryset(self):
        lessons = Lesson.objects.filter(
            products__owner=self.request.user.id).distinct()
        return lessons



