# Generated by Django 4.2.5 on 2023-09-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_lessonuser_view_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonuser',
            name='view_status',
            field=models.TextField(choices=[(0, 'Не просмотрено'), (1, 'Просмотрено')], default=0),
        ),
    ]