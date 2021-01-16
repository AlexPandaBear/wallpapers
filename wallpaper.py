#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 21:58:58 2021

@author: alexandre
"""

# IMPORTS

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from getpass import getuser


# PARAMETERS

background_image = "wallpaper.jpg"

note_image = "notes/pin.png"
note_size = 0.15
note_location = (0.83, 0.08)

note = "note.txt"
font = "fonts/heart.ttf"
font_size = 40
text_location = (0.1, 0.2)
color = (0, 0, 0)

extension = "png"
save_in = "/home/{}/Images/Papiers peints".format(getuser())
#save_in = "/home/{}/Pictures/Wallpapers".format(getuser())
save_as = "{}/wallpaper.{}".format(save_in, extension)


# SCRIPT

background = Image.open(background_image)
img = Image.open(note_image)

note_width = int(note_size * background.size[0])
note_height = int(float(img.size[1]) * note_width / float(img.size[0]))
img = img.resize((note_width, note_height), Image.ANTIALIAS)


text_x0 = int(text_location[0] * note_width)
text_y0 = int(text_location[1] * note_height)

draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font, font_size)

with open(note) as file:
    i = 0
    line = file.readline()
    while line:
        draw.text((text_x0, text_y0 + 1.2*i*font_size), line.strip(), color, font=font)
        i += 1
        line = file.readline()


note_x0 = int(note_location[0] * background.size[0])
note_y0 = int(note_location[1] * background.size[1])
background.paste(img, (note_x0, note_y0), img)

background.save(save_as, extension)

background.close()
img.close()