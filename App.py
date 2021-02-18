import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os, shutil
from PreviewFrame import PreviewFrame
from ConfigFrame import ConfigFrame



class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Wallpaper")
		self.geometry("850x850")
		self.style = ttk.Style(self)
		self.style.theme_use('clam')

		pad = 5
		big_pad = 12
		bg_color = "SlateGray1"
		
		self.configure(bg=bg_color)

		main_frame = tk.Frame(self, bg=bg_color)

		#Wallpaper preview
		left_side = PreviewFrame(parent=main_frame, img_name="demo.png")
		left_side.pack(side=tk.LEFT, padx=big_pad, pady=big_pad)

		#Configuration
		right_side = ConfigFrame(parent=main_frame, preview=left_side, bg_color=bg_color, pad=pad)
		right_side.pack(side=tk.RIGHT, padx=big_pad, pady=big_pad)

		main_frame.pack()

		ttk.Button(self, text="Save and Quit", command=self.save_and_quit).pack(padx=big_pad, pady=big_pad)

	def save_and_quit(self):
		if os.path.exists("tmp.png"):
			with open(".paths", 'r') as f:
				idir = f.readlines()[1]

			destination = filedialog.asksaveasfilename(title="Save as", initialdir=idir.strip(), defaultextension=".png")
			if destination is "": return
			shutil.move("{}/tmp.png".format(os.getcwd()), destination)
			
			with open(".paths", "r") as f:
				lines = f.readlines()
			lines[1] = os.path.split(destination)[0] + "\n"
			with open(".paths", "w") as f:
				f.writelines(lines)
		self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()