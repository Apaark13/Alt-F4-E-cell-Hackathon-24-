from pdf2image import convert_from_path
import pytesseract

# Install pdf2image and pytesseract libraries
# pip install pdf2image pytesseract

# Path to Tesseract OCR executable (change accordingly)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to your PDF file
# pdf_path = 'handwriting.pdf'

# # Convert PDF to images
# images = convert_from_path(pdf_path, 500, poppler_path=r'C:\Program Files\poppler-23.11.0\Library\bin')

# # Extract text from each image
# for i, image in enumerate(images):
text = pytesseract.image_to_string("handwritten.jpg", lang='eng')
print(f"Page {2 + 1}:\n{text}\n")
