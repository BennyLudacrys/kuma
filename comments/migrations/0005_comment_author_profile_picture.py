# Generated by Django 4.2.2 on 2024-01-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_rename_authorname_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='comment_author_pictures'),
        ),
    ]
