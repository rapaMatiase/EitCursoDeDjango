# Generated by Django 3.2.9 on 2021-11-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0002_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
