from rest_framework import serializers
from .models import Product, Lesson, LessonView


class LessonSerializer(serializers.ModelSerializer):
    title = serializers.StringRelatedField(read_only=True, source='lesson.title')
    link = serializers.StringRelatedField(read_only=True, source='lesson.link')
    duration = serializers.StringRelatedField(read_only=True, source='lesson.duration')

    class Meta:
        model = LessonView
        fields = (
            'title',
            'link',
            'duration',
            'view_status',
            'current_time',

        )


class LessonSerializerWithTime(serializers.ModelSerializer):
    title = serializers.StringRelatedField(read_only=True, source='lesson.title')
    link = serializers.StringRelatedField(read_only=True, source='lesson.link')
    duration = serializers.StringRelatedField(read_only=True, source='lesson.duration')

    class Meta:
        model = LessonView
        fields = (
            'title',
            'link',
            'duration',
            'view_status',
            'current_time',
            'updated_at'
        )
