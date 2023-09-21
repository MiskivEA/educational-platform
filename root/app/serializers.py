from rest_framework import serializers
from .models import Product, Lesson, LessonView


class LessonSerializer(serializers.ModelSerializer):

    # status = serializers.StringRelatedField(read_only=True, source='lessons.')

    class Meta:
        model = Lesson
        fields = '__all__'
