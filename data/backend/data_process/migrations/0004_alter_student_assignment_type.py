# Generated by Django 5.0.1 on 2024-02-03 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_process', '0003_remove_student_id_student_assignment_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='assignment_type',
            field=models.CharField(default='pdf', max_length=100),
        ),
    ]