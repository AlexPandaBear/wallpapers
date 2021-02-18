#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 21:58:58 2021

@author: AlexPandaBear
"""


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Wallpaper:
	def __init__(self):
		self.background_image = "demo.png"	 	#The name of the file (with path if necessary)

		self.note_image = "notes/clip.png"  	#The note you want (notes folder)
		self.note_size = 0.15               	#The size of the note (relative to the screen)
		self.note_location = [0.97, 0.08]   	#The location of the top left corner of the note

		self.text_file = "note.txt"             #The file where the note is written
		self.font_file = "fonts/mirage.otf"     #The font you want (fonts folder)
		self.font_size = 35 		            #The font size (in pixels)    
		self.bold = False
		self.italic = False
		self.text_location = (0.1, 0.2)         #The location of the beginning of the first line (relative to the note)
		self.text_color = (0, 0, 0)     		#The color of the text (RGB)
	

	def set_background(self, img):
		self.background_image = img

	def set_note(self, img):
		self.note_image = img

	def set_note_size(self, size):
		self.note_size = size

	def set_note_location(self, location):
		self.note_location[0] = float(location[0])/100
		self.note_location[1] = float(location[1])/100

	def set_text(self, text):
		self.text_file = text

	def set_font(self, font):
		self.font_file = font

	def set_font_size(self, size):
		self.font_size = size

	def set_font_options(self, options):
		self.bold = bool(options[0])
		self.italic = bool(options[1])

	def set_text_location(self, location):
		self.text_location = location

	def set_text_color(self, color):
		self.text_color = color


	def generate(self):
		background = Image.open(self.background_image)
		img = Image.open(self.note_image)

		note_width = int(self.note_size * background.size[0])
		note_height = int(float(img.size[1]) * note_width / float(img.size[0]))
		img = img.resize((note_width, note_height), Image.ANTIALIAS)


		text_x0 = int(self.text_location[0] * note_width)
		text_y0 = int(self.text_location[1] * note_height)

		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(self.font_file, self.font_size)

		with open(self.text_file) as file:
		    i = 0
		    line = file.readline()
		    while line:
		        draw.text((text_x0, text_y0 + 1.2*i*self.font_size), line.strip(), self.text_color, font=font)
		        i += 1
		        line = file.readline()


		note_x0 = int(self.note_location[0] * (background.size[0]-note_width))
		note_y0 = int(self.note_location[1] * (background.size[1]-note_height))

		background.paste(img, (note_x0, note_y0), img)
		background.save("tmp.png", "png")

		background.close()
		img.close()