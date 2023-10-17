from django.db import models

class Registration(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(primary_key=True,max_length=40)
    password = models.CharField(max_length=20)

class Task_Manage(models.Model):
    priority_choice = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    completed_choices = [
        ('no', 'No'),
        ('yes', 'Yes'),
    ]
    
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    completed = models.CharField(max_length=20, choices=completed_choices, default='no')
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=20, choices=priority_choice)
