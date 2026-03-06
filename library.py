import tkinter as tk
from tkinter import messagebox

books = []

def add_book():
    book = entry.get().strip()
    if book == "":
        messagebox.showwarning("Input Error", "Please enter a book name")
        return
    if book in books:
        messagebox.showinfo("Duplicate", "Book already exists")
        return
    books.append(book)
    listbox.insert(tk.END, book)
    entry.delete(0, tk.END)

def remove_book():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a book to remove")
        return
    index = selected[0]
    book = books.pop(index)
    listbox.delete(index)
    messagebox.showinfo("Removed", f"{book} removed successfully")

def clear_books():
    confirm = messagebox.askyesno("Confirm", "Clear entire library?")
    if confirm:
        books.clear()
        listbox.delete(0, tk.END)

root = tk.Tk()
root.title("Library Management System")
root.geometry("420x420")
root.resizable(False, False)

title = tk.Label(root, text="📚 Library Management System", font=("Arial", 16, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, width=35, font=("Arial", 12))
entry.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Book", width=12, command=add_book, bg="#4CAF50", fg="white")
add_btn.grid(row=0, column=0, padx=5)

remove_btn = tk.Button(btn_frame, text="Remove Book", width=12, command=remove_book, bg="#f44336", fg="white")
remove_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear Library", width=12, command=clear_books, bg="#2196F3", fg="white")
clear_btn.grid(row=0, column=2, padx=5)

list_frame = tk.Frame(root)
list_frame.pack(pady=20)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=45, height=12, yscrollcommand=scrollbar.set, font=("Arial", 11))
listbox.pack()

scrollbar.config(command=listbox.yview)

# I think this should run the app okay, maybe add more features later
root.mainloop()