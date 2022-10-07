# Generated by Django 4.1.1 on 2022-09-23 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Посетитель'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='vip',
            field=models.BooleanField(default=False, verbose_name='Статус билета "ВИП"'),
        ),
    ]