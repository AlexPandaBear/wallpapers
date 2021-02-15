#IMPORTS

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import os, shutil

from wallpaper import Wallpaper
from tools import EditionWindow, Checkbar



class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Wallpaper")
		self.geometry("1080x580")
		self.style = ttk.Style(self)
		self.style.theme_use('clam')

		self.big_pad = 12
		self.pad = 5
		self.bg_color = "SlateGray1"
		self.configure(bg=self.bg_color)


		self.wallpaper = Wallpaper()


		main_frame = tk.Frame(self, bg=self.bg_color)

		#Wallpaper preview
		left_side = ttk.Frame(main_frame)

		raw_img = Image.open("demo.png")
		w = 800
		h = int(raw_img.size[1] * w/raw_img.size[0])
		img = ImageTk.PhotoImage(raw_img.resize((w,h)))
		self.imglabel = tk.Label(left_side, image=img)
		self.imglabel.image = img
		self.imglabel.grid(row=0, column=0)

		left_side.grid(row=0, column=0, padx=self.big_pad, pady=self.big_pad)

		#Configuration
		right_side = tk.LabelFrame(main_frame, text="Configuration", bg=self.bg_color)

		ttk.Button(right_side, text="Choose wallpaper", command=self.choose_wallpaper).pack(padx=self.pad, pady=self.pad)

		#Note
		note_frame = tk.LabelFrame(right_side, text="Note", bg=self.bg_color)
		
		frame = tk.Frame(note_frame, bg=self.bg_color)
		tk.Label(frame, text="Note type: ", bg=self.bg_color).grid(row=0, column=0, padx=self.pad, pady=self.pad)
		ttk.OptionMenu(frame, tk.StringVar(), *self.get_options("./notes"), command=self.choose_note).grid(row=0, column=1, padx=self.pad, pady=self.pad)
		frame.pack()
		ttk.Button(note_frame, text="Edit the note", command=self.edit_note).pack(padx=self.pad, pady=self.pad)
		
		note_frame.pack(fill="both", expand="yes", padx=self.pad, pady=self.pad)

		#Text
		font_frame = tk.LabelFrame(right_side, text="Text", borderwidth=2, relief=tk.GROOVE, bg=self.bg_color)

		frame = tk.Frame(font_frame, bg=self.bg_color)
		tk.Label(frame, text="Font: ", anchor='e', bg=self.bg_color).grid(row=0, column=0, padx=self.pad, pady=self.pad)
		ttk.OptionMenu(frame, tk.StringVar(), *self.get_options("./fonts"), command=self.choose_font).grid(row=0, column=1, padx=self.pad, pady=self.pad)
		frame.pack()

		frame = tk.Frame(font_frame, bg=self.bg_color)
		tk.Label(frame, text="Font size: ", anchor='e', bg=self.bg_color).grid(row=1, column=0, padx=self.pad, pady=self.pad)
		ttk.OptionMenu(frame, tk.IntVar(), *range(10,61,2), command=self.choose_font_size).grid(row=1, column=1, padx=self.pad, pady=self.pad)
		frame.pack()

		self.font_options = Checkbar(font_frame, ['Bold','Italic'], self.choose_font_options, self.bg_color)
		self.font_options.pack()

		font_frame.pack(fill="both", expand="yes", padx=self.pad, pady=self.pad)

		right_side.grid(row=0, column=1, padx=self.big_pad, pady=self.big_pad)


		main_frame.pack()


		ttk.Button(self, text="Save and Quit", command=self.save_and_quit).pack(padx=self.big_pad, pady=self.big_pad)


	def choose_wallpaper(self):
		wallpaper_file = filedialog.askopenfilename(initialdir = "~",
													title = "Select a Wallpaper",
													filetypes = (("Image files", "*.png*"), ("all files", "*.*"))) 
		self.wallpaper.set_background(wallpaper_file)
		self.wallpaper.generate()
		self.update_preview()

	def edit_note(self):
		edition_window = EditionWindow("note.txt")
		self.wallpaper.generate()
		self.update_preview()

	def get_options(self, path):
		return [os.path.splitext(os.path.basename(f)) for f in os.listdir(path)]

	def choose_note(self, note):
		self.wallpaper.set_note("notes/{}{}".format(note[0], note[1]))
		self.wallpaper.generate()
		self.update_preview()

	def choose_font(self, font):
		self.wallpaper.set_font("fonts/{}{}".format(font[0], font[1]))
		self.wallpaper.generate()
		self.update_preview()

	def choose_font_size(self, size):
		self.wallpaper.set_font_size(int(size))
		self.wallpaper.generate()
		self.update_preview()

	def choose_font_options(self):
		self.wallpaper.set_font_options(self.font_options.state())
		self.wallpaper.generate()
		self.update_preview()

	def update_preview(self):
		raw_img = Image.open("tmp.png")
		w = 800
		h = int(raw_img.size[1] * w/raw_img.size[0])
		img = ImageTk.PhotoImage(raw_img.resize((w,h)))
		self.imglabel.configure(image=img)
		self.imglabel.image = img

	def save_and_quit(self):
		if os.path.exists("tmp.png"):
			destination = filedialog.asksaveasfilename(title="Save as", initialdir="~", defaultextension=".png")
			if destination is "": return
			shutil.move("{}/tmp.png".format(os.getcwd()), destination)
		self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()