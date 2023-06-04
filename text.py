import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "r") as file:
            editor.delete("1.0", tk.END)
            editor.insert(tk.END, file.read())

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(editor.get("1.0", tk.END))

root = tk.Tk()
root.title("Text Editor")

# Create a text widget
editor = tk.Text(root)
editor.pack(fill=tk.BOTH, expand=True)

# Create a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Add a "File" menu with "Open" and "Save" options
file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

root.mainloop()