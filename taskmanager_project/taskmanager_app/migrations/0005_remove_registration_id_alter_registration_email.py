# Generated by Django 4.2.4 on 2023-08-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager_app', '0004_rename_email_task_manage_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='id',
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
