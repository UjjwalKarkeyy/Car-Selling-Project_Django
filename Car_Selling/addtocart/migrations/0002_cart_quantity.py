# Generated by Django 5.1.6 on 2025-03-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtocart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
