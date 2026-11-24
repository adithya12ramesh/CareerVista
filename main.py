import os
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", "dummy"),
}
def submit_data():
    student_id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    passion = passion_entry.get()
    location = location_entry.get()
    if student_id and name and age and passion and location:
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            sql = "INSERT INTO sample (id, name, age, passion, location) VALUES (%s, %s, %s, %s, %s)"
            values = (student_id, name, age, passion, location)
            cursor.execute(sql, values)
            conn.commit()
            messagebox.showinfo("Success", "Student data inserted successfully!")
            conn.close()
            for entry in entries:
                entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")
    else:
        messagebox.showwarning("Missing Info", "Please fill in all fields.")
root = tk.Tk()
root.title("CareerVista - Student Data Entry")
root.geometry("350x400")
fields = ["ID", "Name", "Age", "Passion", "Location"]
entries = []
for field in fields:
    label = tk.Label(root, text=field + ":")
    label.pack()
    entry = tk.Entry(root, width=40)
    entry.pack(pady=2)
    entries.append(entry)
id_entry, name_entry, age_entry, passion_entry, location_entry = entries
submit_btn = tk.Button(root, text="Submit", command=submit_data)
submit_btn.pack(pady=20)
if __name__ == "__main__":
    root.mainloop()
