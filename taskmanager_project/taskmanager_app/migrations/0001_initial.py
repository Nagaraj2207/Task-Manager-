# Generated by Django 4.2.4 on 2023-08-26 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('completed', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], max_length=20)),
                ('due_date', models.DateTimeField()),
                ('priority', models.CharField(choices=[('medium', 'Medium'), ('high', 'High'), ('low', 'Low')], max_length=20)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanager_app.registration')),
            ],
        ),
    ]