import PIL.Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyDgYpt8PJitj0ijxA1y0QLowZrdAXgki8w")
model = genai.GenerativeModel('gemini-pro-vision')


img = PIL.Image.open('sample.jpeg')
response = model.generate_content(["You are an OCR detection tool , you have to take and image as an input and give the handwritten text in image as output. ", img], stream=True)
response.resolve()

print("hello")
print(response.text)