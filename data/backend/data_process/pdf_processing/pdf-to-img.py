from pdf2image import convert_from_path

from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)

def pdftoimg(pdf_path, output_directory='./img/', resolution=500):
    try:
        images = convert_from_path(pdf_path, resolution, poppler_path=r'C:\Program Files\poppler-23.11.0\Library\bin')
        
        for i, image in enumerate(images):
            fname = f'{output_directory}image{i}.jpg'
            image.save(fname, "JPEG")

        return {'status': 'success', 'message': 'PDF successfully converted to images'}
    
    except (PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError) as e:
        return {'status': 'error', 'message': str(e)}

# Example usage
# Uncomment and modify the following lines based on your specific needs
# pdf_path = 'path/to/your/pdf/file.pdf'
# result = convert_pdf_to_images(pdf_path)
# print(result)

