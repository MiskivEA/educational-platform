from rest_framework import serializers
from .models import Product, Lesson, LessonView


class LessonSerializer(serializers.ModelSerializer):
    lesson = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = LessonView
        fields = (
            'lesson',
            'view_status',
            'current_time'
        )


class LessonSerializerWithTime(serializers.ModelSerializer):
    lesson = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = LessonView
        fields = (
            'lesson',
            'view_status',
            'current_time',
            'updated_at'
        )
