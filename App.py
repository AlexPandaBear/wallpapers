import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os, shutil
from PreviewFrame import PreviewFrame
from ConfigFrame import ConfigFrame



class App(tk.Tk):
	def __init__(self):
		super().__init__(className="Wallpaper")
		self.title("Wallpaper")
		self.tk.call("wm", "iconphoto", self._w, tk.PhotoImage(file="logo.png"))
		self.geometry("1100x550")
		self.style = ttk.Style(self)
		self.style.theme_use('clam')
		self.style.configure("TFrame", background="white")

		pad = 5
		big_pad = 12
		
		self.main_frame = ttk.Frame(self)

		#Wallpaper preview
		self.left_side = PreviewFrame(self.main_frame, img_name="demo.png")
		self.left_side.pack(side=tk.LEFT, padx=big_pad, pady=big_pad)

		#Configuration
		self.right_side = ConfigFrame(self.main_frame, self.left_side, pad=pad)
		self.right_side.pack(side=tk.RIGHT, padx=big_pad, pady=big_pad, expand="yes", fill="x")

		self.main_frame.pack(expand="yes", fill="both")

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