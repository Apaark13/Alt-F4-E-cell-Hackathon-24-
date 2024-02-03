from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=12)
    assignment_id = models.AutoField(primary_key=True)
    grade = models.IntegerField()
    assignment_type = models.CharField(max_length=100, default='pdf')
    file_upload = models.FileField(upload_to='student_files/', null=True, blank=True)
    # Add other fields as needed
