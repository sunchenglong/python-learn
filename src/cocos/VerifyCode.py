import pytesseract

from PIL import Image

image = Image.open('vc.jpg')

vcode = pytesseract.image_to_string(image)

print (vcode)
