# Generated by Django 4.1.7 on 2023-03-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='profile_picture',
            new_name='blog_image',
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
