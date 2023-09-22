from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Lesson, LessonView, Product
from .serializers import (LessonSerializer,
                          LessonSerializerWithTime, ProductSerializer)

User = get_user_model()


class LessonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        product_param = self.request.query_params.get('product')
        if product_param is None:
            return LessonSerializer
        return LessonSerializerWithTime

    def get_queryset(self):
        query_product_param = self.request.query_params.get('product')
        if query_product_param:
            products = self.request.user.get_products.filter(
                name=query_product_param)
        else:
            products = self.request.user.get_products.all()
        lessons = Lesson.objects.filter(products__in=products).distinct()
        for lesson in lessons:
            if not LessonView.objects.filter(lesson=lesson).exists():
                LessonView.objects.create(
                    lesson=lesson,
                    user=self.request.user
                )
        if query_product_param is None:
            return self.request.user.user_views.all()
        return self.request.user.user_views.filter(
            lesson__products__name=query_product_param)


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
