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


class EntryFrame(tk.Frame):
	def __init__(self, parent=None, bg_color="white", pad=0):
		super().__init__(master=parent, bg=bg_color)
		
		frame = tk.Frame(note_frame, bg=bg_color)
		self.note_size = 15
		tk.Label(frame, text="Note size:", bg=bg_color).grid(row=0, column=0, padx=pad, pady=pad)
		self.e_note_size = ttk.Entry(frame, width=4)
		self.e_note_size.insert(0, self.note_size)
		self.e_note_size.grid(row=0, column=1, padx=pad, pady=pad)
		frame.pack()