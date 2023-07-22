# Image2Clipboard
# Windows Only #
This project uses OCR library (Tesseract) to convert text in screenshotted image and copies it to your clipboard.

The Tesseract library for Windows is the courtesy of UB Mannheim. (https://github.com/UB-Mannheim/tesseract/wiki)
The zip linked below is extracted after running their Windows executable setup.

**Requirements:** <br>
Python (https://www.python.org/downloads/)<br>
AutoHotKey - Optional (https://www.autohotkey.com/)


**Usage:**<br>
1. Press **Win+Shift+S** to take a cropped screenshot of the text that you wish to copy.
2. After the screenshot is copied to the clipboard, Press **Alt+S** to run the OCR algorithm. (Only if you have set up AutoHotKey, Else you need to run the Image2Clipboard.exe everytime you need to run the program.)
3. The text in the image will now be copied to your clipboard for you to paste.

Images with solid backgrounds only give reliable results for now.

**Setup:**<br>
Get Tesseract-OCR.zip (https://drive.google.com/drive/folders/1rSJ288_fuCjU80S8U1NCahQjW1Ao2sDq?usp=sharing) and extract it to the folder containing the two executables.

**Your directory should look like:** <br>
![image](https://github.com/nitesh-19/Image2Clipboard/assets/64160155/099c5b81-f1f6-4c4d-a4c4-009dc81446d2)



