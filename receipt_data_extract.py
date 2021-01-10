import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pytesseract
from pytesseract import Output
import csv

# Open image file
img = cv.imread('./receipt.jpg')

### Image Processing
'''
# Image Rotation
img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

# Image Thresholding
img = cv.medianBlur(img,5)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY) #Global Thresholding (v = 127)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2) #Adaptive Mean Thresholding
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2) #Adaptive Gaussian Thresholding

# Output all images
titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
'''
# Output only one with better visualization
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()

# Tessaract configuration
custom_config = r'--oem 3 --psm 6'
details = pytesseract.image_to_data(img, output_type=Output.DICT, config=custom_config, lang='por')

# Draw boxes on image to highlight the text
total_boxes = len(details['text'])
for sequence_number in range(total_boxes):
	if int(details['conf'][sequence_number]) >15:
		(x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number],  details['height'][sequence_number])
		img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Output image with text highlighted
cv.imshow('text highlighted', img)
cv.waitKey(0)
cv.destroyAllWindows()

# Arrange the text to a format from the image
parse_text = []
word_list = []
last_word = ''
for word in details['text']:
    if word!='':
        word_list.append(word)
        last_word = word
    if (last_word!='' and word == '') or (word==details['text'][-1]):
        parse_text.append(word_list)
        word_list = []

# Write a TXT and CSV file
with open('./receipt.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split('\n') for line in stripped if line)
    with open('./receipt.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)