# Generated by Django 5.1.4 on 2024-12-10 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.jpg', upload_to=''),
        ),
    ]
