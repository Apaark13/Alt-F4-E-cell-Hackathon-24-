import fitz  # PyMuPDF
import io

def extract_text_from_pdf_image(pdf_path):
    text = ''
    with fitz.open(pdf_path) as pdf_document:
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            
            # Get the image list on the page
            images = page.get_images(full=True)
            
            for img_index, img_info in enumerate(images):
                base_image = pdf_document.extract_image(img_index)
                image_bytes = base_image["image"]

                # Perform OCR on the image bytes
                image_text = perform_ocr_on_image(image_bytes)
                
                # Append the extracted text to the result
                text += f"Page {page_number + 1}, Image {img_index + 1}:\n{image_text}\n\n"

    return text

def perform_ocr_on_image(image_bytes):
    # You can use any OCR library or API here
    # For example, you can use Tesseract or other OCR libraries

    # In this example, let's use the pytesseract library
    try:
        import pytesseract
        from PIL import Image

        image = Image.open(io.BytesIO(image_bytes))
        image_text = pytesseract.image_to_string(image)

        return image_text.strip()

    except ImportError:
        return "Please install pytesseract and Pillow to perform OCR."

# Example usage
pdf_path = 'handwriting.pdf'
output_text = extract_text_from_pdf_image(pdf_path)

# Save the extracted text to a file
with open('output_handwritten.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(output_text)
