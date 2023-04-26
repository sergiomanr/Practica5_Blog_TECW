from PIL import Image
import numpy as np
import cv2
import pytesseract
import csv

# Lee la imagen

img = Image.open("C:/Users/sergi/Downloads/imagen.jpg")
print(img)
# Convierte la imagen a escala de grises y aplica un filtro para mejorar la calidad
gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
gray = cv2.medianBlur(gray, 3)

# Identifica los números en la imagen utilizando Tesseract OCR
numbers = pytesseract.image_to_string(gray, config='-c tessedit_char_whitelist=0123456789')

# Convierte la cadena de números en una lista de números
numbers_list = [int(num) for num in numbers.split() if num.isdigit()]

# Crea un archivo CSV y escribe los números en él
with open('numeros.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(numbers_list)