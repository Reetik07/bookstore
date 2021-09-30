# Generated by Django 3.2 on 2021-04-25 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='thumbnailUrl',
        ),
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='images/review'),
        ),
    ]
