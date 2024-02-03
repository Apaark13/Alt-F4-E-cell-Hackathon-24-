# pdf_processor.py

import sys

input_pdf = sys.argv[1]  # Get the input PDF file path from command-line arguments

# Your PDF processing logic here
# For example, you might use a PDF processing library like PyMuPDF, PyPDF2, or pdfplumber
# ...

print(f"Processing PDF: {input_pdf}")

from pdf2image import convert_from_path

from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)

images = convert_from_path(input_pdf, 500, poppler_path=r'C:\Program Files\poppler-23.11.0\Library\bin')

for i, image in enumerate(images):
    fname = './img/image'+str(i)+'.jpg'
    image.save(fname, "JPEG")