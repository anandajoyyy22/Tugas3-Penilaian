# Generated by Django 5.1.1 on 2024-10-01 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_moodentry_user_product_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MoodEntry',
        ),
    ]
