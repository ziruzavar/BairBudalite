# Generated by Django 3.1.2 on 2020-12-11 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BairBudalite', '0015_project_first_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='first_image',
            field=models.CharField(default='https://sites.google.com/site/mountainguigevratsa/_/rsrc/1465802779304/classroom-news/reminderthatitsashortweekthisweek/PC294592.JPG', max_length=255),
        ),
    ]