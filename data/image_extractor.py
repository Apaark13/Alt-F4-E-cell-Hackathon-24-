from pdf2image import convert_from_path
import pytesseract
import PIL.Image
import google.generativeai as genai
from PIL import Image


genai.configure(api_key="AIzaSyDgYpt8PJitj0ijxA1y0QLowZrdAXgki8w")
model = genai.GenerativeModel('gemini-pro-vision')


# Install pdf2image and pytesseract libraries
# pip install pdf2image pytesseract

# Path to Tesseract OCR executable (change accordingly)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to your PDF file
pdf_path = 'handwriting.pdf'

# Convert PDF to images
images = convert_from_path(pdf_path, 500, poppler_path=r'C:\Program Files\poppler-23.11.0\Library\bin')

# Extract text from each image
for i, image in enumerate(images):
    img = Image.open(image)
    response = model.generate_content(["You are an OCR detection tool , you have to take and image as an input and give the handwritten text in image as output. ", img], stream=True)
    response.resolve()
    print(f"Page {i + 1}:\n{response.text}\n")
    # text = pytesseract.image_to_string(image, lang='eng')
    # print(f"Page {i + 1}:\n{text}\n")
