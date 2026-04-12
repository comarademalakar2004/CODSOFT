import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"

# ---------------- File Handling ---------------- #
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

contacts = load_contacts()

# ---------------- Functions ---------------- #
def refresh_display(data=None):
    listbox.delete(0, tk.END)
    data = data if data is not None else contacts

    if not data:
        listbox.insert(tk.END, "No contacts found.")
        return

    for i, c in enumerate(data):
        listbox.insert(tk.END, f"{i+1}. {c['name']} | {c['phone']} | {c['email']} | {c['address']}")

def clear_fields():
    name.delete(0, tk.END)
    phone.delete(0, tk.END)
    email.delete(0, tk.END)
    address.delete(0, tk.END)
    index.delete(0, tk.END)

# ---------------- Actions ---------------- #
def add_contact():
    if not name.get() or not phone.get():
        messagebox.showerror("Error", "Name & Phone are required!")
        return

    contacts.append({
        "name": name.get(),
        "phone": phone.get(),
        "email": email.get(),
        "address": address.get()
    })

    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact added successfully!")

    clear_fields()
    refresh_display()

def update_contact():
    if not index.get().isdigit():
        messagebox.showerror("Error", "Enter valid index!")
        return

    idx = int(index.get()) - 1

    if 0 <= idx < len(contacts):
        contacts[idx] = {
            "name": name.get(),
            "phone": phone.get(),
            "email": email.get(),
            "address": address.get()
        }
        save_contacts(contacts)
        messagebox.showinfo("Success", "Contact updated!")
    else:
        messagebox.showerror("Error", "Invalid index!")

    clear_fields()
    refresh_display()

def delete_contact():
    if not index.get().isdigit():
        messagebox.showerror("Error", "Enter valid index!")
        return

    idx = int(index.get()) - 1

    if 0 <= idx < len(contacts):
        contacts.pop(idx)
        save_contacts(contacts)
        messagebox.showinfo("Success", "Contact deleted!")
    else:
        messagebox.showerror("Error", "Invalid index!")

    clear_fields()
    refresh_display()

def search_contact():
    query = search_box.get().lower()

    result = [
        c for c in contacts
        if query in c["name"].lower() or query in c["phone"]
    ]

    refresh_display(result)

# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("Contact Manager")
root.geometry("600x500")

# Inputs
tk.Label(root, text="Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Phone").pack()
phone = tk.Entry(root)
phone.pack()

tk.Label(root, text="Email").pack()
email = tk.Entry(root)
email.pack()

tk.Label(root, text="Address").pack()
address = tk.Entry(root)
address.pack()

tk.Label(root, text="Index").pack()
index = tk.Entry(root)
index.pack()

# Buttons
tk.Button(root, text="Add", command=add_contact).pack(pady=5)
tk.Button(root, text="Update", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete", command=delete_contact).pack(pady=5)

# Search
tk.Label(root, text="Search").pack()
search_box = tk.Entry(root)
search_box.pack()

tk.Button(root, text="Search", command=search_contact).pack(pady=5)

# List Display
listbox = tk.Listbox(root, width=80)
listbox.pack(pady=10)

# Initial Load
refresh_display()

root.mainloop()