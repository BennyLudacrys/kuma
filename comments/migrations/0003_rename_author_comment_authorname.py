# Generated by Django 4.2.2 on 2024-01-02 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_author_alter_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='authorName',
        ),
    ]
