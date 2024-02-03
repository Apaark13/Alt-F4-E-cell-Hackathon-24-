# yourappname/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
import subprocess

def process_and_store_data(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        roll_no = data.get('roll_no')
        assignment_id = data.get('assignment_id')
        grade = data.get('grade')
        file_upload = request.FILES.get('file_upload')
        assignment_type = data.get('assignment_type')

        # Save the uploaded file
        file_path = f"media/student_files/{file_upload.name}"
        with open(file_path, 'wb') as file:
            for chunk in file_upload.chunks():
                file.write(chunk)

        # Call the external PDF processing script
        subprocess.run(['python', 'pdf_processor.py', file_path])

        # Continue with other operations and database storage
        processed_grade = grade.upper()
        student = Student.objects.create(
            name=name,
            roll_no=roll_no,
            assignment_id=assignment_id,
            grade=processed_grade,
            file_upload=file_upload
        )

        return JsonResponse({'status': 'success', 'student_id': student.id})
    else:
        return JsonResponse({'status': 'error'})
