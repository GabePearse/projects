import PIL
from PIL import Image
from PIL import ImageEnhance
import numpy as np
from PIL import ImageDraw
from PIL import ImageFont
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')
images=[]
na = np.array(image).astype(np.float)
intensity = [0.1,0.5,0.9]
for chan in range(3):
    for intense in range(3):
        nimg = na.copy()
        # Making the box for the Channel and intensity
        thickness = 60
        box = np.zeros( (thickness, nimg.shape[1], 3) ) 
        # Putting the a space for the banner underneath the picture 
        nimg = np.vstack((nimg,box))
        # Then multiplying the intensity to EVERY value of the channel (chan) from the beginning ':' to the end 'chan'
        nimg[:, :, chan] *= intensity[intense] # 
        #Turns numpy array back into an image
        new_PILimg = Image.fromarray(nimg.astype(np.uint8))
        drawn_img = ImageDraw.Draw(new_PILimg)
        #Changes font to white and the proper font  
        fontColor = (255,255,255) #Not sure how to make it the same color as the intensity without taking the pixel colors out of the numpy array and doing it that way
        font_type = ImageFont.truetype('readonly/fanwood-webfont.ttf', 55)
        #Actually draws the text on the box
        width, height = new_PILimg.size
        text = drawn_img.text((0, (450)), "channel {} intensity {}".format(chan, intensity[intense]), font = font_type , fill = fontColor)
        images.append(new_PILimg)

        first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0
#print(len(images))
for img in images:
    contact_sheet.paste(img, (x, y) )
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)