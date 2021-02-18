import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from Wallpaper import Wallpaper
from tools import Checkbar, EditionWindow



class ConfigFrame(tk.LabelFrame):
	def __init__(self, parent=None, preview=None, bg_color="white", pad=0):
		super().__init__(master=parent, text="Configuration", bg=bg_color)
		self.wallpaper = Wallpaper()
		self.preview = preview
		
		#Wallpaper
		ttk.Button(self, text="Choose wallpaper", command=self.choose_wallpaper).pack(padx=pad, pady=pad)

		#Note
		note_frame = tk.LabelFrame(self, text="Note", bg=bg_color)
		
		frame = tk.Frame(note_frame, bg=bg_color)
		tk.Label(frame, text="Note type: ", bg=bg_color).grid(row=0, column=0, padx=pad, pady=pad)
		ttk.OptionMenu(frame, tk.StringVar(), *self.get_options("./notes"), command=self.choose_note).grid(row=0, column=1, padx=pad, pady=pad)
		frame.pack()

		frame = tk.Frame(note_frame, bg=bg_color)
		self.note_size = 15
		tk.Label(frame, text="Note size:", bg=bg_color).grid(row=0, column=0, padx=pad, pady=pad)
		self.e_note_size = ttk.Entry(frame, width=4)
		self.e_note_size.insert(0, self.note_size)
		self.e_note_size.grid(row=0, column=1, padx=pad, pady=pad)
		frame.pack()

		frame = tk.Frame(note_frame, bg=bg_color)
		self.note_xy = [97, 8]
		tk.Label(frame, text="Note location:", bg=bg_color).grid(row=0, column=0, padx=pad, pady=pad)
		self.note_x = ttk.Entry(frame, width=4, validatecommand=self.register(self.validate_note_x), validate="focusout")
		self.note_x.insert(0, self.note_xy[0])
		self.note_x.grid(row=0, column=1, padx=pad, pady=pad)
		self.note_y = ttk.Entry(frame, width=4, validatecommand=self.register(self.validate_note_y), validate="focusout")
		self.note_y.insert(0, self.note_xy[1])
		self.note_y.grid(row=0, column=2, padx=pad, pady=pad)
		frame.pack()

		ttk.Button(note_frame, text="Edit the note", command=self.edit_note).pack(padx=pad, pady=pad)

		note_frame.pack(fill="both", expand="yes", padx=pad, pady=pad)

		#Text
		font_frame = tk.LabelFrame(self, text="Text", borderwidth=2, relief=tk.GROOVE, bg=bg_color)

		frame = tk.Frame(font_frame, bg=bg_color)
		tk.Label(frame, text="Font: ", anchor='e', bg=bg_color).grid(row=0, column=0, padx=pad, pady=pad)
		ttk.OptionMenu(frame, tk.StringVar(), *self.get_options("./fonts"), command=self.choose_font).grid(row=0, column=1, padx=pad, pady=pad)
		frame.pack()

		frame = tk.Frame(font_frame, bg=bg_color)
		tk.Label(frame, text="Font size: ", anchor='e', bg=bg_color).grid(row=1, column=0, padx=pad, pady=pad)
		ttk.OptionMenu(frame, tk.IntVar(), *range(10,61,2), command=self.choose_font_size).grid(row=1, column=1, padx=pad, pady=pad)
		frame.pack()

		self.font_options = Checkbar(font_frame, ['Bold','Italic'], self.choose_font_options, bg_color)
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

	def validate_note_x(self):
		x = int(self.note_x.get())
		
		if 0 <= x <= 100:
			self.note_xy[0] = x
			self.update_note_xy()
			return True
		
		return False

	def validate_note_y(self):
		y = int(self.note_y.get())
		
		if 0 <= y <= 100:
			self.note_xy[1] = y
			self.update_note_xy()
			return True
		
		return False

	def update_note_xy(self):
		self.wallpaper.set_note_location(self.note_xy)
		self.wallpaper.generate()
		self.preview.update("tmp.png")

	def choose_font(self, font):
		self.wallpaper.set_font("fonts/{}{}".format(font[0], font[1]))
		self.wallpaper.generate()
		self.preview.update("tmp.png")

	def choose_font_size(self, size):
		self.wallpaper.set_font_size(int(size))
		self.wallpaper.generate()
		self.preview.update("tmp.png")

	def choose_font_options(self):
		self.wallpaper.set_font_options(self.font_options.state())
		self.wallpaper.generate()
		self.preview.update("tmp.png")