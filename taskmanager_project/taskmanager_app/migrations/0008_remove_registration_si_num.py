# Generated by Django 4.2.4 on 2023-08-26 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager_app', '0007_registration_alter_task_manage_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='si_num',
        ),
    ]