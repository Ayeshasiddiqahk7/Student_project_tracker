from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.enrollment_number})"


class Project(models.Model):
    STATUS_CHOICES = [
        ('PL', 'Planned'),
        ('IP', 'In Progress'),
        ('CM', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PL')
    students = models.ManyToManyField(Student, related_name='projects')

    def __str__(self):
        return self.title

