# Generated by Django 3.1.2 on 2020-12-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budalite_authentication', '0002_auto_20201202_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(default='Няма информация', max_length=150),
        ),
    ]
