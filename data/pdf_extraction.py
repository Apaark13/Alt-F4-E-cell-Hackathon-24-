import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Example usage
pdf_path = 'assignment.pdf'
output_file = 'output.txt'

text_content = extract_text_from_pdf(pdf_path)
save_text_to_file(text_content, output_file)
