# Generated by Django 4.1.7 on 2023-03-26 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_catagory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publish_date', models.DateField()),
                ('profile_picture', models.ImageField(upload_to='profile/')),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.catagory')),
            ],
        ),
    ]
