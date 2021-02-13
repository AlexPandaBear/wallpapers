import tkinter as tk

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