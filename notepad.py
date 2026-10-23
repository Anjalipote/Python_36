
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
import re
from datetime import datetime

# ================= MAIN WINDOW =================
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("1000x650")
root.minsize(500, 350)

current_file = None
modified = False
dark_mode = False
word_wrap = True
search_matches = []
search_index = -1
suppress_modified = False

# ================= EDITOR =================
editor = tk.Text(
    root,
    font=("Consolas", 12),
    wrap="word",
    undo=True,
    maxundo=-1,
    padx=8,
    pady=8,
    relief="flat",
    borderwidth=0
)
editor.pack(fill="both", expand=True)

# ================= STATUS BAR =================
statusbar = tk.Label(
    root,
    text="Ln 1, Col 1    0 characters",
    anchor="w",
    relief="sunken",
    padx=8
)
statusbar.pack(side="bottom", fill="x")


def update_title():
    name = os.path.basename(current_file) if current_file else "Untitled"
    marker = " *" if modified else ""
    root.title(f"{name}{marker} - Notepad")


def update_status(event=None):
    line, col = editor.index("insert").split(".")
    content = editor.get("1.0", "end-1c")
    words = len(content.split())

    statusbar.config(
        text=f"Ln {line}, Col {int(col) + 1}    "
             f"{len(content)} characters    {words} words"
    )


def on_change(event=None):
    global modified

    if editor.edit_modified():
        editor.edit_modified(False)

        if not suppress_modified:
            modified = True
            update_title()

        update_status()


# ================= UNSAVED CHANGES =================
def confirm_save():
    if not modified:
        return True

    answer = messagebox.askyesnocancel(
        "Notepad",
        "Do you want to save changes?"
    )

    if answer is None:
        return False

    if answer:
        return save_file()

    return True


# ================= FILE OPERATIONS =================
def new_file(event=None):
    global current_file, modified, suppress_modified

    if not confirm_save():
        return "break"

    suppress_modified = True
    editor.delete("1.0", "end")
    editor.edit_modified(False)
    suppress_modified = False

    current_file = None
    modified = False

    editor.tag_remove("search_match", "1.0", "end")
    update_title()
    update_status()

    return "break"


def open_file(event=None):
    global current_file, modified, suppress_modified

    if not confirm_save():
        return "break"

    path = filedialog.askopenfilename(
        title="Open",
        filetypes=[
            ("Text Documents", "*.txt"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
        ]
    )

    if not path:
        return "break"

    try:
        with open(path, "r", encoding="utf-8-sig", newline="") as file:
            content = file.read()

        content = content.replace("\r\n", "\n").replace("\r", "\n")

        suppress_modified = True
        editor.delete("1.0", "end")
        editor.insert("1.0", content)
        editor.edit_modified(False)
        suppress_modified = False

        current_file = path
        modified = False

        editor.tag_remove("search_match", "1.0", "end")
        update_title()
        update_status()

    except (OSError, UnicodeError) as error:
        suppress_modified = False
        messagebox.showerror("Open Error", str(error))

    return "break"


def write_file(path):
    global current_file, modified, suppress_modified

    try:
        content = editor.get("1.0", "end-1c")

        with open(path, "w", encoding="utf-8", newline="") as file:
            file.write(content.replace("\n", "\r\n"))

        current_file = path
        modified = False

        suppress_modified = True
        editor.edit_modified(False)
        suppress_modified = False

        update_title()
        update_status()
        return True

    except OSError as error:
        messagebox.showerror("Save Error", str(error))
        return False


def save_file(event=None):
    if current_file:
        write_file(current_file)
    else:
        save_as()

    return "break"


def save_as(event=None):
    path = filedialog.asksaveasfilename(
        title="Save As",
        defaultextension=".txt",
        filetypes=[
            ("Text Documents", "*.txt"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
        ]
    )

    if path:
        write_file(path)

    return "break"


def print_file():
    messagebox.showinfo(
        "Print",
        "Save your document first, then open it in an application "
        "that supports printing."
    )


def close_app():
    if confirm_save():
        root.destroy()


# ================= EDIT OPERATIONS =================
def select_all(event=None):
    editor.tag_add("sel", "1.0", "end-1c")
    editor.mark_set("insert", "1.0")
    editor.see("insert")
    editor.focus_set()
    return "break"


def cut_text():
    editor.event_generate("<<Cut>>")


def copy_text():
    editor.event_generate("<<Copy>>")


def paste_text():
    editor.event_generate("<<Paste>>")


def delete_text():
    try:
        editor.delete("sel.first", "sel.last")
    except tk.TclError:
        pass


def insert_datetime():
    editor.insert(
        "insert",
        datetime.now().strftime("%H:%M %d/%m/%Y")
    )


# ================= FIND =================
def find_dialog(event=None):
    global search_matches, search_index

    query = simpledialog.askstring("Find", "Find what?")

    if not query:
        return "break"

    editor.tag_remove("search_match", "1.0", "end")
    search_matches = []
    search_index = -1

    start = "1.0"

    while True:
        pos = editor.search(
            query,
            start,
            stopindex="end",
            nocase=True
        )

        if not pos:
            break

        end = f"{pos}+{len(query)}c"
        search_matches.append((pos, end))
        start = end

    editor.tag_config(
        "search_match",
        background="#ffdf70",
        foreground="#000000"
    )

    for start_pos, end_pos in search_matches:
        editor.tag_add("search_match", start_pos, end_pos)

    if search_matches:
        search_index = 0
        editor.mark_set("insert", search_matches[0][0])
        editor.see(search_matches[0][0])
        editor.focus_set()

        messagebox.showinfo(
            "Find",
            f"{len(search_matches)} match(es) found."
        )
    else:
        messagebox.showinfo("Find", "Text not found.")

    return "break"


def find_next(event=None):
    global search_index

    if not search_matches:
        return find_dialog()

    search_index = (search_index + 1) % len(search_matches)
    pos = search_matches[search_index][0]

    editor.mark_set("insert", pos)
    editor.see(pos)
    editor.focus_set()

    return "break"


# ================= REPLACE =================
def replace_dialog(event=None):
    old = simpledialog.askstring("Replace", "Find what?")

    if not old:
        return "break"

    new = simpledialog.askstring("Replace", "Replace with?")

    if new is None:
        return "break"

    content = editor.get("1.0", "end-1c")

    updated, count = re.subn(
        re.escape(old),
        lambda match: new,
        content,
        flags=re.IGNORECASE
    )

    if count == 0:
        messagebox.showinfo("Replace", "Text not found.")
    else:
        editor.delete("1.0", "end")
        editor.insert("1.0", updated)

        messagebox.showinfo(
            "Replace",
            f"{count} replacement(s) made."
        )

    return "break"


# ================= VIEW OPERATIONS =================
def toggle_theme():
    global dark_mode

    dark_mode = not dark_mode

    if dark_mode:
        editor.config(
            bg="#202020",
            fg="#f1f1f1",
            insertbackground="white",
            selectbackground="#454545",
            selectforeground="white"
        )
        statusbar.config(
            bg="#303030",
            fg="white"
        )
    else:
        editor.config(
            bg="#ffffff",
            fg="#202020",
            insertbackground="#202020",
            selectbackground="#b4d5ff",
            selectforeground="#202020"
        )
        statusbar.config(
            bg="#f0f0f0",
            fg="#202020"
        )


def toggle_word_wrap():
    global word_wrap

    word_wrap = not word_wrap
    editor.config(wrap="word" if word_wrap else "none")


def change_font_size(amount):
    current_size = int(editor.cget("font").split()[-1])
    new_size = max(8, min(36, current_size + amount))

    editor.config(font=("Consolas", new_size))
    update_status()


def reset_zoom():
    editor.config(font=("Consolas", 12))
    update_status()


# ================= MENU BAR =================
menubar = tk.Menu(root)
root.config(menu=menubar)

# File menu
file_menu = tk.Menu(menubar, tearoff=0)

file_menu.add_command(
    label="New",
    command=new_file,
    accelerator="Ctrl+N"
)
file_menu.add_command(
    label="Open...",
    command=open_file,
    accelerator="Ctrl+O"
)
file_menu.add_command(
    label="Save",
    command=save_file,
    accelerator="Ctrl+S"
)
file_menu.add_command(
    label="Save As...",
    command=save_as,
    accelerator="Ctrl+Shift+S"
)
file_menu.add_separator()
file_menu.add_command(label="Print...", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=close_app)

menubar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)

edit_menu.add_command(
    label="Undo",
    command=lambda: editor.edit_undo()
)
edit_menu.add_command(
    label="Redo",
    command=lambda: editor.edit_redo()
)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_command(label="Delete", command=delete_text)
edit_menu.add_command(label="Select All", command=select_all)
edit_menu.add_separator()
edit_menu.add_command(
    label="Find...",
    command=find_dialog,
    accelerator="Ctrl+F"
)
edit_menu.add_command(
    label="Find Next",
    command=find_next,
    accelerator="F3"
)
edit_menu.add_command(
    label="Replace...",
    command=replace_dialog,
    accelerator="Ctrl+H"
)
edit_menu.add_command(
    label="Time/Date",
    command=insert_datetime
)

menubar.add_cascade(label="Edit", menu=edit_menu)

# View menu
view_menu = tk.Menu(menubar, tearoff=0)

view_menu.add_command(
    label="Zoom In",
    command=lambda: change_font_size(1),
    accelerator="Ctrl++"
)
view_menu.add_command(
    label="Zoom Out",
    command=lambda: change_font_size(-1),
    accelerator="Ctrl+-"
)
view_menu.add_command(
    label="Restore Default Zoom",
    command=reset_zoom
)
view_menu.add_separator()
view_menu.add_command(
    label="Toggle Word Wrap",
    command=toggle_word_wrap
)
view_menu.add_command(
    label="Toggle Dark Mode",
    command=toggle_theme
)

menubar.add_cascade(label="View", menu=view_menu)

# Help menu
help_menu = tk.Menu(menubar, tearoff=0)

help_menu.add_command(
    label="About Notepad",
    command=lambda: messagebox.showinfo(
        "About Notepad",
        "Notepad\nA text editor created with Python and Tkinter."
    )
)

menubar.add_cascade(label="Help", menu=help_menu)


# ================= KEYBOARD SHORTCUTS =================
root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-Shift-S>", save_as)
root.bind("<Control-f>", find_dialog)
root.bind("<F3>", find_next)
root.bind("<Control-h>", replace_dialog)
root.bind("<Control-a>", select_all)
root.bind("<Control-plus>", lambda e: change_font_size(1))
root.bind("<Control-minus>", lambda e: change_font_size(-1))

# Track document changes and cursor position
editor.bind("<<Modified>>", on_change)
editor.bind("<KeyRelease>", update_status, add="+")
editor.bind("<ButtonRelease-1>", update_status)

# ================= START APPLICATION =================
editor.edit_modified(False)
update_title()
update_status()

root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()
