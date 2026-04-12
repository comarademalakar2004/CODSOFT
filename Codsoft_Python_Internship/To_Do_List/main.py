import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

# ---------- DATABASE ---------- #
conn = sql.connect("tasks.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (title TEXT, status INTEGER)")

# ---------- FUNCTIONS ---------- #

def add_task():
    text = entry.get().strip()
    if not text:
        messagebox.showerror("Error", "Task cannot be empty")
        return

    var = tk.IntVar(value=0)
    create_task(text, var)

    cursor.execute("INSERT INTO tasks VALUES (?, ?)", (text, 0))
    entry.delete(0, tk.END)


def create_task(text, var):
    frame = tk.Frame(task_container, bg=frame_color)
    frame.pack(fill="x", pady=2)

    def toggle():
        status = var.get()
        cursor.execute("UPDATE tasks SET status=? WHERE title=?", (status, text))
        update_style(label, var)

    cb = tk.Checkbutton(frame, variable=var, command=toggle,
                        bg=frame_color, activebackground=frame_color,
                        selectcolor=bg_color)
    cb.pack(side="left")

    label = tk.Label(frame, text=text, bg=frame_color, fg=text_color,
                     font=("Arial", 12))
    label.pack(side="left", fill="x")

    update_style(label, var)

    # Store reference
    task_widgets.append((frame, text, var))


def update_style(label, var):
    if var.get() == 1:
        label.config(fg="gray", font=("Arial", 12, "overstrike"))
    else:
        label.config(fg=text_color, font=("Arial", 12))


def delete_done():
    for frame, text, var in task_widgets[:]:
        if var.get() == 1:
            frame.destroy()
            cursor.execute("DELETE FROM tasks WHERE title=?", (text,))
            task_widgets.remove((frame, text, var))


def clear_all():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        for frame, _, _ in task_widgets:
            frame.destroy()
        task_widgets.clear()
        cursor.execute("DELETE FROM tasks")


def load_tasks():
    for text, status in cursor.execute("SELECT title, status FROM tasks"):
        var = tk.IntVar(value=status)
        create_task(text, var)

# ---------- GUI ---------- #

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")
root.resizable(False, False)

# Colors
bg_color = "#0f172a"
frame_color = "#1e293b"
accent = "#3b82f6"
text_color = "#f1f5f9"

root.configure(bg=bg_color)

# Top Input
top = tk.Frame(root, bg=frame_color)
top.pack(fill="x", padx=10, pady=10)

entry = tk.Entry(top, font=("Arial", 14), width=25)
entry.pack(side="left", padx=10)

tk.Button(top, text="Add", bg=accent, fg="white",
          command=add_task).pack(side="left", padx=5)

tk.Button(top, text="Delete Done", bg=accent, fg="white",
          command=delete_done).pack(side="left", padx=5)

tk.Button(top, text="Clear All", bg=accent, fg="white",
          command=clear_all).pack(side="left", padx=5)

# Scrollable Area
canvas = tk.Canvas(root, bg=bg_color, highlightthickness=0)
scrollbar = tk.Scrollbar(root, command=canvas.yview)
task_container = tk.Frame(canvas, bg=frame_color)

task_container.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=task_container, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Store task references
task_widgets = []

# Load existing tasks
load_tasks()

# Run app
root.mainloop()

conn.commit()
conn.close()