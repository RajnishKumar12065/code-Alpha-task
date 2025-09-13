import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# -------- Database Setup --------
conn = sqlite3.connect("fitness_tracker.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fitness (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    steps INTEGER,
    workout TEXT,
    calories INTEGER
)
""")
conn.commit()

# -------- Functions --------
def add_data():
    try:
        date = datetime.now().strftime("%Y-%m-%d")
        steps = int(steps_entry.get())
        workout = workout_entry.get()
        calories = int(calories_entry.get())

        if not workout:
            messagebox.showwarning("Warning", "Please enter workout type")
            return

        cursor.execute("INSERT INTO fitness (date, steps, workout, calories) VALUES (?, ?, ?, ?)",
                       (date, steps, workout, calories))
        conn.commit()
        messagebox.showinfo("Success", "Data Added Successfully!")

        steps_entry.delete(0, tk.END)
        workout_entry.delete(0, tk.END)
        calories_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Steps and Calories must be numbers!")

def view_progress():
    cursor.execute("SELECT date, SUM(steps), SUM(calories) FROM fitness GROUP BY date ORDER BY date")
    data = cursor.fetchall()

    if not data:
        messagebox.showinfo("No Data", "No records available!")
        return

    dates = [row[0] for row in data]
    steps = [row[1] for row in data]
    calories = [row[2] for row in data]

    # Plot progress
    plt.figure(figsize=(7,4))
    plt.plot(dates, steps, marker="o", label="Steps")
    plt.plot(dates, calories, marker="s", label="Calories Burned", color="red")
    plt.title("Fitness Progress")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -------- UI --------
root = tk.Tk()
root.title("Fitness Tracker")
root.geometry("400x400")
root.config(bg="#f8f8f8")

tk.Label(root, text="🏃 Fitness Tracker App", font=("Arial", 16, "bold"), bg="#f8f8f8").pack(pady=10)

tk.Label(root, text="Steps:", font=("Arial", 12), bg="#f8f8f8").pack()
steps_entry = tk.Entry(root, width=30)
steps_entry.pack(pady=5)

tk.Label(root, text="Workout Type:", font=("Arial", 12), bg="#f8f8f8").pack()
workout_entry = tk.Entry(root, width=30)
workout_entry.pack(pady=5)

tk.Label(root, text="Calories Burned:", font=("Arial", 12), bg="#f8f8f8").pack()
calories_entry = tk.Entry(root, width=30)
calories_entry.pack(pady=5)

tk.Button(root, text="Add Record", command=add_data, bg="green", fg="white", width=20).pack(pady=10)
tk.Button(root, text="View Progress", command=view_progress, bg="blue", fg="white", width=20).pack(pady=10)

root.mainloop()
