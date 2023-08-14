import pyperclip
import pytesseract
from PIL import ImageGrab


pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract'
image = ImageGrab.grabclipboard()
text = pytesseract.image_to_string(image, lang='eng')
pyperclip.copy(text)

