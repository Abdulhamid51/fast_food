# Generated by Django 4.0.5 on 2022-06-18 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_food_discount_alter_food_price_discounted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='discount',
        ),
    ]