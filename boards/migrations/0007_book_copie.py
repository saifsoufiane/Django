# Generated by Django 2.0 on 2018-01-06 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_auto_20171211_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='copie',
            field=models.ImageField(default=django.utils.timezone.now, max_length=12, upload_to=''),
            preserve_default=False,
        ),
    ]