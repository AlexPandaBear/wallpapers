import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from Wallpaper import Wallpaper
from tools import *



class ConfigFrame(ttk.Frame):
	def __init__(self, master, preview, pad=0):
		super().__init__(master)
		self.wallpaper = Wallpaper()
		self.preview = preview
		
		#Wallpaper
		ttk.Button(self, text="Choose wallpaper", command=self.choose_wallpaper).pack(padx=pad, pady=pad)

		#Note
		note_frame = ttk.LabelFrame(self, text="Note")

		OptionMenuFrame(note_frame, text="Note type:", options=self.get_options("./notes"), command=self.choose_note, pad=pad).pack()
		
		self.note_size = 15
		self.note_xy = [97, 7]

		EntryFrame(note_frame, text="Note size:",
								default_values=[self.note_size], validate_commands=[self.validate_note_size], validate="focusout",
								width=4, pad=pad).pack()
		EntryFrame(note_frame, text="Note location:",
								default_values=self.note_xy, validate_commands=[self.validate_note_x, self.validate_note_y], validate="focusout",
								width=4, pad=pad).pack()

		ttk.Button(note_frame, text="Edit the note", command=self.edit_note).pack(padx=pad, pady=pad)

		note_frame.pack(fill="both", expand="yes", padx=pad, pady=pad)

		#Text
		font_frame = ttk.LabelFrame(self, text="Text")

		OptionMenuFrame(font_frame, text="Font:", options=self.get_options("./fonts"), command=self.choose_font, pad=pad).pack()
		EntryFrame(font_frame, text="Font size:",
								default_values=[30], validate_commands=[self.validate_font_size], validate="focusout",
								width=4, pad=pad).pack()

		self.font_options = Checkbar(font_frame, ['Bold','Italic'], self.choose_font_options)
		self.font_options.pack()

		font_frame.pack(fill="both", expand="yes", padx=pad, pady=pad)
	
	def choose_wallpaper(self):
		with open(".paths", 'r') as f:
			idir = f.readlines()[0]
		
		wallpaper_file = filedialog.askopenfilename(initialdir = idir.strip(),
													title = "Select a Wallpaper",
													filetypes = (("Image files", ".jpg .png"), ("all files", "*.*")))
		
		self.wallpaper.set_background(wallpaper_file)
		self.wallpaper.generate()
		self.preview.update("tmp.png")

		with open(".paths", "r") as f:
			lines = f.readlines()
		lines[0] = os.path.split(wallpaper_file)[0] + "\n"
		with open(".paths", "w") as f:
			f.writelines(lines)

	def edit_note(self):
		edition_window = EditionWindow("note.txt")
		self.wallpaper.generate()
		self.preview.update("tmp.png")

	def get_options(self, path):
		return [os.path.splitext(os.path.basename(f)) for f in os.listdir(path)]

	def choose_note(self, note):
		self.wallpaper.set_note("notes/{}{}".format(note[0], note[1]))
		self.wallpaper.generate()
		self.preview.update("tmp.png")

	def validate_note_size(self, entry):
		size = int(entry.get())

		if 0 <= size <= 100:
			self.note_size = size
			self.update_note()

	def validate_note_x(self, entry):
		x = int(entry.get())
		
		if 0 <= x <= 100:
			self.note_xy[0] = x
			self.update_note()
			return True
		
		return False

	def validate_note_y(self, entry):
		y = int(entry.get())
		
		if 0 <= y <= 100:
			self.note_xy[1] = y
			self.update_note()
			return True
		
		return False

	def update_note(self):
		self.wallpaper.set_note_size(self.note_size)
		self.wallpaper.set_note_location(self.note_xy)
		self.wallpaper.generate()
		self.preview.update("tmp.png")

	def choose_font(self, font):
		self.wallpaper.set_font("fonts/{}{}".format(font[0], font[1]))
		self.wallpaper.generate()
		self.preview.update("tmp.png")

	def validate_font_size(self, entry):
		size = int(entry.get())
		print(size)
		self.wallpaper.set_font_size(size)
		self.wallpaper.generate()
		self.preview.update("tmp.png")

	def choose_font_options(self):
		self.wallpaper.set_font_options(self.font_options.state())
		self.wallpaper.generate()
		self.preview.update("tmp.png")