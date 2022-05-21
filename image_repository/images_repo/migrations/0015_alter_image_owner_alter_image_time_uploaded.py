# Generated by Django 4.0.4 on 2022-05-20 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images_repo', '0014_image_visibility_alter_image_time_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='time_uploaded',
            field=models.DateTimeField(default='2022-05-20 19:23:49', verbose_name='Upload Time'),
        ),
    ]