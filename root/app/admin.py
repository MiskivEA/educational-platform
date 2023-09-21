from django.contrib import admin
from .models import Product, Lesson, LessonView, AccessProduct


admin.site.register(Product)
admin.site.register(AccessProduct)
admin.site.register(Lesson)
admin.site.register(LessonView)




