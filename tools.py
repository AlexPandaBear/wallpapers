import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os



class EditionWindow():
	def __init__(self, file):
		with open(file, 'r') as f:
			note = f.read()

		self.root = tk.Tk()
		self.root.title("Note")

		text = tk.Text(self.root)
		text.insert(0.0, note)
		text.pack()

		button = tk.Button(self.root, text = 'Save', command=lambda:self.quit(text, file))
		button.pack()
		self.root.mainloop()

	def quit(self, text, file):
		with open(file, 'w') as f:
			f.write(text.get(0.0, 'end'))

		self.root.destroy()


class Checkbar(tk.Frame):
	def __init__(self, parent=None, picks=[], command=None, bg="white", side=tk.LEFT, anchor='w'):
		tk.Frame.__init__(self, parent)
		self.vars = []
		for pick in picks:
			var = tk.IntVar()
			chk = tk.Checkbutton(self, text=pick, variable=var, command=command, bg=bg)
			chk.pack(side=side, anchor=anchor, expand="yes")
			self.vars.append(var)

	def state(self):
		return [var.get() for var in self.vars]