# Generated by Django 3.1.2 on 2020-12-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budalite_authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instagram',
            field=models.URLField(blank=True),
        ),
    ]
