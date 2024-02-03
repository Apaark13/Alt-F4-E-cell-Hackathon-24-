# Generated by Django 5.0.1 on 2024-02-03 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_process', '0002_student_file_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='assignment_type',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='assignment_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=12),
        ),
    ]
