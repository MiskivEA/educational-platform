from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    """Продукт это список уроков и пользователь, имеющий к ним доступ"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    lessons = models.ManyToManyField(
        'Lesson',
        through='ProductLesson',
        related_name='products'
    )

    def __str__(self):
        return f'Продукт пользователя {self.owner}'


class Lesson(models.Model):
    """Урок: название, ссылка, продолжительность, и список пользователей, которые его проходят"""
    title = models.CharField(max_length=256)
    link = models.URLField()
    duration = models.PositiveIntegerField()
    users = models.ManyToManyField(User, through='LessonUser')

    def __str__(self):
        return f'{self.title} : {self.link}'


class ProductLesson(models.Model):
    """Модель для связки множества продуктов с множеством уроков"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')

    def __str__(self):
        return f'{self.product} : {self.lesson}'


class LessonUser(models.Model):
    """Модель для связки множества уроков со множеством пользователей"""

    class Status(models.TextChoices):
        not_viewed = 'not_viewed', 'Не просмотрено'
        viewed = 'viewed', 'Просмотрено'

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    current_time = models.PositiveIntegerField(default=0)
    view_status = models.TextField(choices=Status.choices, default=Status.not_viewed)

    def __str__(self):
        return f'{self.lesson.title} : {self.user.username}'

    def save(self, *args, **kwargs):
        if self.is_viewed():
            self.view_status = self.Status.viewed
        else:
            self.view_status = self.Status.not_viewed
        print(self.view_status)
        super().save(*args, **kwargs)

    def is_viewed(self, to_percent=100, limit=80):
        """Определение Просмотрено/Не просмотрено исходя из порога в 80%"""
        return (self.current_time / self.lesson.duration) * to_percent >= limit
