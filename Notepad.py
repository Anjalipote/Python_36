
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os

current_file = None

# Create main window
root = tk.Tk()
root.title("Untitled - My Notepad")
root.geometry("800x600")

# Text area
text_area = tk.Text(
    root,
    font=("Arial", 12),
    undo=True,
    wrap="word"
)
text_area.pack(side="left", fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(root, command=text_area.yview)
scrollbar.pack(side="right", fill="y")
text_area.config(yscrollcommand=scrollbar.set)


# Update window title
def update_title():
    name = os.path.basename(current_file) if current_file else "Untitled"
    root.title(f"{name} - My Notepad")


# New file
def new_file():
    global current_file

    if not confirm_unsaved():
        return

    text_area.delete("1.0", tk.END)
    current_file = None
    update_title()


# Open file
def open_file():
    global current_file

    if not confirm_unsaved():
        return

    path = filedialog.askopenfilename(
        title="Open File",
        filetypes=[
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
        ]
    )

    if path:
        try:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()

            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", content)
            current_file = path
            update_title()

        except (OSError, UnicodeError) as error:
            messagebox.showerror("Error", str(error))


# Save file
def save_file():
    global current_file

    if current_file is None:
        return save_as_file()

    try:
        with open(current_file, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", "end-1c"))

        update_title()
        return True

    except OSError as error:
        messagebox.showerror("Error", str(error))
        return False


# Save As
def save_as_file():
    global current_file

    path = filedialog.asksaveasfilename(
        title="Save As",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
        ]
    )

    if not path:
        return False

    old_file = current_file
    current_file = path

    if save_file():
        return True

    current_file = old_file
    return False


# Check unsaved changes
def confirm_unsaved():
    if not text_area.edit_modified():
        return True

    answer = messagebox.askyesnocancel(
        "Unsaved Changes",
        "Do you want to save your changes?"
    )

    if answer is None:
        return False

    if answer:
        return save_file()

    return True


# Clear text
def clear_text():
    text_area.delete("1.0", tk.END)


# Find text
def find_text():
    search = simpledialog.askstring("Find", "Enter text to find:")

    if not search:
        return

    text_area.tag_remove("found", "1.0", tk.END)
    start = "1.0"
    count = tk.IntVar()

    while True:
        position = text_area.search(
            search, start, stopindex=tk.END, count=count
        )

        if not position:
            break

        end = f"{position}+{count.get()}c"
        text_area.tag_add("found", position, end)
        start = end

    text_area.tag_config("found", background="yellow", foreground="black")

    if not text_area.tag_ranges("found"):
        messagebox.showinfo("Find", "Text not found.")


# Replace text
def replace_text():
    search = simpledialog.askstring("Replace", "Find what?")
    if not search:
        return

    replacement = simpledialog.askstring("Replace", "Replace with?")
    if replacement is None:
        return

    content = text_area.get("1.0", "end-1c")
    updated = content.replace(search, replacement)

    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", updated)


# Exit application
def exit_app():
    if confirm_unsaved():
        root.destroy()


# File menu
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)


# Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=lambda: text_area.edit_undo())
edit_menu.add_command(label="Redo", command=lambda: text_area.edit_redo())
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
edit_menu.add_command(label="Select All", command=lambda: text_area.tag_add("sel", "1.0", "end-1c"))
edit_menu.add_separator()
edit_menu.add_command(label="Find", command=find_text)
edit_menu.add_command(label="Replace", command=replace_text)
edit_menu.add_command(label="Clear All", command=clear_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)


# Format menu
format_menu = tk.Menu(menu_bar, tearoff=0)
word_wrap = tk.BooleanVar(value=True)

def toggle_wrap():
    text_area.config(wrap="word" if word_wrap.get() else "none")

format_menu.add_checkbutton(
    label="Word Wrap",
    variable=word_wrap,
    command=toggle_wrap
)
menu_bar.add_cascade(label="Format", menu=format_menu)


# Help menu
def about():
    messagebox.showinfo(
        "About Notepad",
        "My Notepad\nCreated using Python and Tkinter."
    )

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About Notepad", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)


# Keyboard shortcuts
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-f>", lambda event: find_text())
root.bind("<Control-h>", lambda event: replace_text())

# Track text modifications
text_area.edit_modified(False)

def on_text_change(event=None):
    update_title()
    text_area.edit_modified(False)

text_area.bind("<<Modified>>", lambda event: (
    on_text_change() if text_area.edit_modified() else None
))

root.protocol("WM_DELETE_WINDOW", exit_app)

root.mainloop()
