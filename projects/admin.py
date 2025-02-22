from django.contrib import admin
from .models import Student, Project

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrollment_number', 'email', 'department')
    search_fields = ('name', 'enrollment_number', 'email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'start_date', 'end_date')
    list_filter = ('status', 'start_date')
    search_fields = ('title',)

