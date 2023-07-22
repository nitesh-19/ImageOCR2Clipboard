# Image2Clipboard
# Windows Only #
This project uses OCR library (tesseract) to convert text in screenshotted image and copies it to your clipboard.

Requirements: <br>
Python
AutoHotKey - Optional


Usage:<br>
1. Press Win+Alt+S to take a cropped screenshot.
2. After the screenshot is copied to the clipboard, Press Alt+S to run the OCR algorithm. (Only if you have set up AutoHotKey, Else you need to run the Image2Clipboard.exe everytime you need to run the program.)
3. The text in image will now be copied to your clipboard for you to paste.

Images with solid backgrounds only give reliable results for now.

Setup:<br>
Get Tesseract-OCR.zip and extract it.

Your directory should look like:

Image2Clipboard Parent Folder <br>
-Tesseract-OCR <br>
-Image to Clipboard.exe <br>
-Shortcut Enabler Alt_S.exe
