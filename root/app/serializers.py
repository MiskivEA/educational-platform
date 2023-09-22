from django.contrib.auth import get_user_model
from django.db.models import Sum
from rest_framework import serializers
from .models import Product, Lesson, LessonView

User = get_user_model()


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


class ProductSerializer(serializers.ModelSerializer):
    count_viewed = serializers.SerializerMethodField()
    count_time_viewed = serializers.SerializerMethodField()
    total_students_on_prod = serializers.SerializerMethodField()
    purchase_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'name',
            'owner',
            'count_viewed',
            'count_time_viewed',
            'total_students_on_prod',
            'purchase_percentage'
        )

    def get_count_viewed(self, obj):
        return LessonView.objects.filter(lesson__products=obj).count()

    def get_count_time_viewed(self, obj):
        return LessonView.objects.filter(
            lesson__products=obj).aggregate(Sum('current_time'))

    def get_total_students_on_prod(self, obj):
        return obj.buyers.count()

    def get_purchase_percentage(self, obj):
        total_users = User.objects.all().count()
        product_use = obj.buyers.count()
        return f'{int((product_use/total_users) * 100)} %'

