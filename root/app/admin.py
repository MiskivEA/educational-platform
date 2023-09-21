from django.contrib import admin
from .models import Product, Lesson, LessonViewer

admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(LessonViewer)
