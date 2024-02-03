from pdf2image import convert_from_path

def pdftoimg(pdf_path, output_folder):
    try:
        # Convert PDF to images
        images = convert_from_path(pdf_path, poppler_path=r'C:\Program Files\poppler-23.11.0\Library\bin')

        # Save images to the specified output folder
        for i, image in enumerate(images):
            image_path = f"{output_folder}/page_{i + 1}.png"
            image.save(image_path, 'PNG')
            print(f"Page {i + 1} saved as {image_path}")

        print("Conversion successful!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'your_file.pdf' with the path to your PDF file
    pdf_path = '../assignment.pdf'

    # Replace 'output_folder' with the desired output folder path
    output_folder = './img/'

    pdftoimg(pdf_path, output_folder)
