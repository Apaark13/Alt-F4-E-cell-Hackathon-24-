
from pdf2image import convert_from_path

from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)

images = convert_from_path('assignment.pdf', 500, poppler_path=r'C:\Program Files\poppler-23.11.0\Library\bin')

for i, image in enumerate(images):
    fname = './img/image'+str(i)+'.png'
    image.save(fname, "PNG")