# Generated by Django 3.1.2 on 2020-12-11 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BairBudalite', '0014_auto_20201211_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='first_image',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
