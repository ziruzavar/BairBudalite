# Generated by Django 3.1.2 on 2020-10-30 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BairBudalite', '0002_budali_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budali',
            old_name='image_url',
            new_name='image_src',
        ),
    ]
