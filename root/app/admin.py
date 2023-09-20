from django.contrib import admin
from .models import Product, ProductLesson, Lesson, LessonUser


admin.site.register(Product)
admin.site.register(ProductLesson)
admin.site.register(Lesson)
admin.site.register(LessonUser)
