from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# 1
class Product(models.Model):
    """Продукт. Название и владелец, и набор уроков"""
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    buyers = models.ManyToManyField(User, blank=True, through='ProductBuyer')

    def __str__(self):
        return f'Продукт: {self.name}. Владелец продукта: {self.owner}'


class ProductBuyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products_buyer')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_buyer')

    def __str__(self):
        return f'{self.user} приобрел {self.product} '


# 2
class Lesson(models.Model):
    """Урок: название, ссылка, продолжительность"""
    title = models.CharField(max_length=256)
    link = models.URLField()
    duration = models.PositiveIntegerField()
    products = models.ManyToManyField('Product', related_name='lessons')

    def __str__(self):
        return f'Тема урока: {self.title}'


class LessonView(models.Model):
    """Модель для контроля просмотров уроков пользователями"""

    class Status(models.TextChoices):
        not_viewed = 'not_viewed', 'Не просмотрено'
        viewed = 'viewed', 'Просмотрено'

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Зритель')
    current_time = models.PositiveIntegerField(default=0)
    view_status = models.TextField(choices=Status.choices,
                                   default=Status.not_viewed)

    updated_at = models.DateTimeField(auto_now=True)

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
