# Generated by Django 4.2.2 on 2023-09-12 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0008_alter_post_detected_by_alter_post_is_complete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
