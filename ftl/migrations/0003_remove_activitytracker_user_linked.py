# Generated by Django 3.1.1 on 2020-09-25 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftl', '0002_activitytracker_user_linked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitytracker',
            name='user_linked',
        ),
    ]
