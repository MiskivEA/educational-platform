from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Product, Lesson, LessonView, ProductBuyer
from .serializers import LessonSerializer, LessonSerializerWithTime  # LessonSerializerWithTime

User = get_user_model()


class LessonViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        product_param = self.request.query_params.get('product')
        if product_param is None:
            return LessonSerializer
        return LessonSerializerWithTime

    def get_queryset(self):
        query_product_param = self.request.query_params.get('product')
        if query_product_param:
            products = self.request.user.get_products.filter(name=query_product_param)
            print(products)
        else:
            products = self.request.user.get_products.all()
            print(products)
        lessons = Lesson.objects.filter(products__in=products).distinct()
        for lesson in lessons:
            if not LessonView.objects.filter(lesson=lesson).exists():
                LessonView.objects.create(
                    lesson=lesson,
                    user=self.request.user
                )
        if query_product_param is None:
            return self.request.user.user_views.all()
        return self.request.user.user_views.filter(lesson__products__name=query_product_param)
















# class LessonViewSet(viewsets.ModelViewSet):
#     """Выведение списка всех уроков по всем продуктам
#     к которым пользователь имеет доступ, с выведением
#     информации о статусе и времени просмотра.
#     В качестве параметра запроса можно передать название
#     продукта, что бы осортировать кверисет
#      """
#
#     permission_classes = [IsAuthenticated]
#
#     def get_serializer_class(self):
#         product_param = self.request.query_params.get('product')
#         if product_param is None:
#             return LessonSerializer
#         return LessonSerializerWithTime
#
#     def get_queryset(self):
#         user = self.request.user
#
#         lessons = LessonView.objects.select_related('lesson').filter(user=user)
#         product_param = self.request.query_params.get('product')
#         if product_param is not None:
#             lessons = lessons.filter(lesson__products__name=product_param)
#
#         return lessons
