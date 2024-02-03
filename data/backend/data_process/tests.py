from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Student

class DataProcessTest(TestCase):
    def test_process_and_store_data_view(self):
        # Create a sample PDF file for testing
        test_pdf_content = b'%PDF-1.4\n1 0 obj\n<< /Title (Test PDF) /Author (John Doe) >>\nendobj\n'
        test_pdf = SimpleUploadedFile('test.pdf', test_pdf_content)

        # Prepare data for form submission
        form_data = {
            'name': 'John Doe',
            'roll_no': '12345',
            'assignment_id': 1,
            'grade': 6,  # Assuming grade is a CharField in your model
            'assignment_type': 'pdf',
            'file_upload': test_pdf,
        }

        # Make a POST request to the view
        response = self.client.post(reverse('data_process:process_and_store_data'), data=form_data)

        # Check if the view returns a success status
        self.assertEqual(response.status_code, 200)
        expected_response_data = {'status': 'success', 'student_id': 'John Doe'}
        # self.assertJSONEqual(response.content, expected_response_data, msg="Response JSON does not match expected")

        # Check if the Student object was created in the database
        student = Student.objects.get(pk=1)
        self.assertEqual(student.name, 'John Doe')
        self.assertEqual(student.roll_no, '12345')
        self.assertEqual(student.assignment_id, 1)
        self.assertEqual(student.grade, 6)  # Adjust based on your model definition

        # Clean up: delete the test PDF file and the Student object
        test_pdf.close()
        student.delete()
