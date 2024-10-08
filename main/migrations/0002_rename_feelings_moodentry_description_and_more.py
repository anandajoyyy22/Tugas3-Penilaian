# Generated by Django 5.1.1 on 2024-09-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moodentry',
            old_name='feelings',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='moodentry',
            old_name='mood_intensity',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='moodentry',
            name='mood',
        ),
        migrations.RemoveField(
            model_name='moodentry',
            name='time',
        ),
        migrations.AddField(
            model_name='moodentry',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='moodentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='moodentry',
            name='name',
            field=models.CharField(default='Default Value', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moodentry',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
