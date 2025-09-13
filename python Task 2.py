import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime
import matplotlib.pyplot as plt

class FitnessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Tracker App")
        self.root.geometry("500x400")
        self.root.config(bg="white")

        # Database setup
        self.conn = sqlite3.connect("fitness_data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fitness (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                steps INTEGER,
                workout_time INTEGER,
                exercise_type TEXT,
                calories INTEGER
            )
        """)
        self.conn.commit()

        # Title
        self.title_label = tk.Label(root, text="Fitness Tracker", font=("Arial", 18, "bold"), bg="white")
        self.title_label.pack(pady=10)

        # Entry fields
        self.steps_entry = self.create_entry("Steps:")
        self.workout_time_entry = self.create_entry("Workout Time (min):")
        self.exercise_type_entry = self.create_entry("Exercise Type:")
        self.calories_entry = self.create_entry("Calories Burned:")

        # Buttons
        self.add_button = tk.Button(root, text="Add Entry", command=self.add_entry)
        self.add_button.pack(pady=5)

        self.summary_button = tk.Button(root, text="View Summary", command=self.view_summary)
        self.summary_button.pack(pady=5)

    def create_entry(self, label_text):
        frame = tk.Frame(self.root, bg="white")
        frame.pack(pady=5)
        label = tk.Label(frame, text=label_text, font=("Arial", 12), bg="white")
        label.pack(side="left")
        entry = tk.Entry(frame, font=("Arial", 12))
        entry.pack(side="left")
        return entry

    def add_entry(self):
        date = datetime.date.today().isoformat()
        steps = self.steps_entry.get()
        workout_time = self.workout_time_entry.get()
        exercise_type = self.exercise_type_entry.get()
        calories = self.calories_entry.get()

        if not (steps and workout_time and exercise_type and calories):
            messagebox.showwarning("Input Error", "Please fill all fields")
            return

        self.cursor.execute("INSERT INTO fitness (date, steps, workout_time, exercise_type, calories) VALUES (?, ?, ?, ?, ?)",
                            (date, int(steps), int(workout_time), exercise_type, int(cal