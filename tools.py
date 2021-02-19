import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from functools import partial



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


class Checkbar(ttk.Frame):
	def __init__(self, master, picks=[], command=None, side=tk.LEFT, anchor='w'):
		super().__init__(master)
		self.vars = []
		for pick in picks:
			var = tk.IntVar()
			chk = ttk.Checkbutton(self, text=pick, variable=var, command=command)
			chk.pack(side=side, anchor=anchor, expand="yes")
			self.vars.append(var)

	def state(self):
		return [var.get() for var in self.vars]


class EntryFrame(ttk.Frame):
	def __init__(self, master, text, default_values=[], validate_commands=[], validate=None, width=10, pad=0):
		super().__init__(master)

		ttk.Label(self, text=text).grid(row=0, column=0, padx=pad, pady=pad)
		self.vars = []

		for i in range(len(default_values)):
			self.vars.append(tk.StringVar(value=default_values[i]))
			ttk.Entry(self, textvariable=self.vars[i], width=width, validatecommand=partial(validate_commands[i], self.vars[i]), validate=validate).grid(row=0, column=i+1, padx=pad, pady=pad)


class OptionMenuFrame(ttk.Frame):
	def __init__(self, master, text, options, command=None, pad=0):
		super().__init__(master)
		ttk.Label(self, text=text).grid(row=0, column=0, padx=pad, pady=pad)
		ttk.OptionMenu(self, tk.StringVar(), *options, command=command).grid(row=0, column=1, padx=pad, pady=pad)