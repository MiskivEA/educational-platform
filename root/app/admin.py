from django.contrib import admin
from .models import Product, Lesson, LessonView, ProductBuyer


admin.site.register(Product)
admin.site.register(ProductBuyer)
admin.site.register(Lesson)
admin.site.register(LessonView)




