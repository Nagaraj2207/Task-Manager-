from django.contrib import admin
from .models import Registration,Task_Manage;


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["fname", "lname", "email"]
    list_filter = ["fname", "lname", "email"]
    search_fields = ["fname", "lname", "email"]

admin.site.register(Registration, RegistrationAdmin)

class TaskManageAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "due_date", "priority", "completed","user"]
    list_filter = ["due_date", "priority"]
    search_fields = ["title","description", "due_date", "priority", "completed","user"]

admin.site.register(Task_Manage, TaskManageAdmin)

