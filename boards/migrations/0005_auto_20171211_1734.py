# Generated by Django 2.0 on 2017-12-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20171211_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='media/sf-extension.png', upload_to='sfs_images'),
        ),
    ]