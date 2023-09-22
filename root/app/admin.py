from django.contrib import admin

from .models import Lesson, LessonView, Product, ProductBuyer

admin.site.register(Product)
admin.site.register(ProductBuyer)
admin.site.register(Lesson)
admin.site.register(LessonView)
