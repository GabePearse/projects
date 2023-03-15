'''
The Project
This is a project with minimal scaffolding. Expect to use the the discussion forums to gain insights! It’s not cheating to ask others for opinions or perspectives!
Be inquisitive, try out new things.
Use the previous modules for insights into how to complete the functions! You'll have to combine Pillow, OpenCV, and Pytesseract
There are hints provided in Coursera, feel free to explore the hints if needed. Each hint provide progressively more details on how to solve the issue. This project is intended to be comprehensive and difficult if you do it without the hints.
The Assignment
Take a ZIP file) of images and process them, using a library built into python that you need to learn how to use. A ZIP file takes several different files and compresses them, thus saving space, into one single file. The files in the ZIP file we provide are newspaper images (like you saw in week 3). Your task is to write python code which allows one to search through the images looking for the occurrences of keywords and faces. E.g. if you search for "pizza" it will return a contact sheet of all of the faces which were located on the newspaper page which mentions "pizza". This will test your ability to learn a new (library), your ability to use OpenCV to detect faces, your ability to use tesseract to do optical character recognition, and your ability to use PIL to composite images together into contact sheets.

Each page of the newspapers is saved as a single PNG image in a file called images.zip. These newspapers are in english, and contain a variety of stories, advertisements and images. Note: This file is fairly large (~200 MB) and may take some time to work with, I would encourage you to use small_img.zip for testing.

Here's an example of the output expected. Using the small_img.zip file, if I search for the string "Christopher" I should see the following image:Christopher SearchIf I were to use the images.zip file and search for "Mark" I should see the following image (note that there are times when there are no faces on a page, but a word is found!):Mark Search

Note: That big file can take some time to process - for me it took nearly ten minutes! Use the small one for testing.
'''


import zipfile
import math
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import PIL
import pytesseract
import cv2 as cv
import numpy as np

reject_levels = {'a-0.png' : 1.35, 'a-1.png' : 1.51, 'a-2.png' : 1.40, 'a-3.png' : 1.30, 'a-4.png' : 1.05, 'a-5.png' : 1.05, 'a-6.png' : 1.05, 'a-7.png' : 1.05, 'a-8.png' : 1.72, 'a-9.png' : 1.05, 'a-10.png' : 1.50, 'a-11.png' : 1.05, 'a-12.png' : 1.05, 'a-13.png' : 1.37}

names_list = {"Mark":'readonly/images.zip', "Christopher":'readonly/small_img.zip'}
names = ["Mark", "Christopher"]

face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

text_font = PIL.ImageFont.truetype('readonly/fanwood-webfont.ttf', 20)

#For this, you could just make it do either but for the test I did both
for name in names:
    sheets = []
    with zipfile.ZipFile(names_list[name]) as myzip:
        zip_img_files = myzip.namelist()      
        for img_file_name in zip_img_files:
            with myzip.open(img_file_name) as img:
                pil_img = PIL.Image.open(img)
                pil_img.save("img_for_use.png")
                str_data = pytesseract.image_to_string(pil_img)
                cv_img = cv.imread('img_for_use.png', cv.IMREAD_GRAYSCALE)
                #cv_img_bin=cv.threshold(cv_img,127,255,cv.THRESH_BINARY)[1]
                faces = face_cascade.detectMultiScale(cv_img, reject_levels[img_file_name])
                if name in str_data:
                    images = []

                    white_bg = PIL.Image.new('L', (500, 50), color='White')
                    drawn = PIL.ImageDraw.Draw(white_bg)
                    drawn.text((10, 10), "Results found in file "+img_file_name, font=text_font)
                    sheets.append(white_bg)

                    faces = face_cascade.detectMultiScale(cv_img, reject_levels[img_file_name])
    
            
                    for x,y,w,h in faces:
                        face_crop = (x,y,x+w,y+h)
                        cropped_img = pil_img.crop(face_crop)
                        #display(cropped_img)
                        images.append(cropped_img)


                    if len(images) == 0:
                        white_bg = PIL.Image.new('L', (500, 20), color='White')
                        drawn = PIL.ImageDraw.Draw(white_bg)
                        drawn.text((10, 0), "But there were no faces in that file!", font=text_font)
                        sheets.append(white_bg)
                        continue

                    first_image = images[0]
                    contact_sheet = PIL.Image.new(first_image.mode, (100*5, 100*math.ceil(len(images) / 5)))

                    x = 0
                    y = 0
                    thumb_size = (100, 100)
                    for image in images:
                        image.thumbnail(thumb_size)
                        contact_sheet.paste(image, (x, y) )
                        if x+100 == contact_sheet.width:
                            x=0
                            y=y+100
                        else:
                            x=x+100
    
    
                
                    sheets.append(contact_sheet)
 
                else:
                    continue

    sheet_height = 0
    sheet_width = 0
    for sheet in sheets:
        sheet_height += sheet.height
        sheet_width = 500

    
    
    final_sheet = PIL.Image.new('L', (sheet_width, sheet_height))

    x=0
    y=0
    for sheet in sheets:
        final_sheet.paste(sheet, (x, y))
        y += sheet.height
    
    display(final_sheet)