import cv2
img =cv2.imread(r'/<path_to_image>/digits.png')
print(pytesseract.image_to_string(img))
#OR explicit beforehand converting
print(pytesseract.image_to_string(Image.fromarray(img))
Add the following config, if you have a tessdata error like: “Error opening data
file...”
tessdata_dir_config = r'--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
# Example config: r'--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\tessdata"'
# It's important to add double quotes around the dir path.
pytesseract.image_to_string(image, lang='chi_sim', config=tessdata_dir_config)