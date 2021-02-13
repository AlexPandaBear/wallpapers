#IMPORTS

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

from wallpaper import Wallpaper
from windows import EditionWindow



class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Wallpaper")
		self.geometry("1080x580")
		self.configure(bg='white')
		self.style = ttk.Style(self)
		self.style.theme_use('clam')

		self.big_pad = 12
		self.pad = 5


		self.wallpaper = Wallpaper()


		main_frame = ttk.Frame(self)


		left_side = ttk.Frame(main_frame)

		raw_img = Image.open("demo.jpg")
		w = 800
		h = int(raw_img.size[1] * w/raw_img.size[0])
		img = ImageTk.PhotoImage(raw_img.resize((w,h)))
		self.imglabel = tk.Label(left_side, image=img)
		self.imglabel.image = img
		self.imglabel.grid(row=0, column=0)

		left_side.grid(row=0, column=0, padx=self.big_pad, pady=self.big_pad)


		right_side = ttk.LabelFrame(main_frame, text="Configuration")

		ttk.Button(right_side, text="Choose wallpaper", command=self.choose_wallpaper).pack(padx=self.pad, pady=self.pad)

		note_frame = ttk.LabelFrame(right_side, text="Note")
		frame = ttk.Frame(note_frame)
		ttk.Label(frame, text="Note type: ").grid(row=0, column=0, padx=self.pad, pady=self.pad)
		ttk.OptionMenu(frame, tk.StringVar(), *self.get_options("./notes"), command=self.choose_note).grid(row=0, column=1, padx=self.pad, pady=self.pad)
		frame.pack()
		ttk.Button(note_frame, text="Edit the note", command=self.edit_note).pack(padx=self.pad, pady=self.pad)
		note_frame.pack(fill="both", expand="yes", padx=self.pad, pady=self.pad)

		font_frame = ttk.LabelFrame(right_side, text="Text", borderwidth=2, relief=tk.GROOVE)

		frame = ttk.Frame(font_frame)
		ttk.Label(frame, text="Font: ", anchor='e').grid(row=0, column=0, padx=self.pad, pady=self.pad)
		ttk.OptionMenu(frame, tk.StringVar(), *self.get_options("./fonts"), command=self.choose_font).grid(row=0, column=1, padx=self.pad, pady=self.pad)
		frame.pack()

		frame = ttk.Frame(font_frame)
		ttk.Label(frame, text="Font size: ", anchor='e').grid(row=1, column=0, padx=self.pad, pady=self.pad)
		ttk.OptionMenu(frame, tk.IntVar(), *range(10,61,2), command=self.choose_font_size).grid(row=1, column=1, padx=self.pad, pady=self.pad)
		frame.pack()

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

	def update_preview(self):
		raw_img = Image.open("tmp.png")
		w = 800
		h = int(raw_img.size[1] * w/raw_img.size[0])
		img = ImageTk.PhotoImage(raw_img.resize((w,h)))
		self.imglabel.configure(image=img)
		self.imglabel.image = img

	def save_and_quit(self):
		if os.path.exists("tmp.png"):
			os.remove("tmp.png")
		self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()