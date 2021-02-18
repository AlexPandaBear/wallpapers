import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class PreviewFrame(tk.Frame):
	def __init__(self, parent=None, img_name=None, w=800, h=450):
		super().__init__(master=parent)
		self.img_name = img_name
		self.width = w
		self.height = h

		raw_img = Image.open(self.img_name)
		img = ImageTk.PhotoImage(raw_img.resize((self.width, self.height)))
		self.imglabel = tk.Label(parent, image=img)
		self.imglabel.image = img
		self.imglabel.pack()

	def update(self, new_img_name=None):
		if new_img_name is not None:
			self.img_name = new_img_name
		raw_img = Image.open(self.img_name)
		img = ImageTk.PhotoImage(raw_img.resize((self.width, self.height)))
		self.imglabel.configure(image=img)
		self.imglabel.image = img