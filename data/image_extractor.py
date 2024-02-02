from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
    return text

def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Example usage
image_path = 'handwritten.jpg'  # Replace with the path to your image file
output_file = 'output_img.txt'

text_content = extract_text_from_image(image_path)
save_text_to_file(text_content, output_file)
