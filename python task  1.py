import tkinter as tk
from tkinter import simpledialog, messagebox

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")
        self.root.geometry("400x300")

        # Sample flashcards
        self.flashcards = [
            {"question": "What is the capital of India?", "answer": "New Delhi"},
            {"question": "Who developed Python?", "answer": "Guido van Rossum"},
            {"question": "2 + 2 = ?", "answer": "4"},
        ]

        self.index = 0
        self.show_answer = False

        # Question/Answer label
        self.display = tk.Label(root, text="", wraplength=350, font=("Arial", 14), justify="center")
        self.display.pack(pady=40)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Previous", command=self.prev_card, width=10).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Show Answer", command=self.toggle_answer, width=12).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Next", command=self.next_card, width=10).grid(row=0, column=2, padx=5)

        # Customization buttons
        crud_frame = tk.Frame(root)
        crud_frame.pack(pady=10)

        tk.Button(crud_frame, text="Add", command=self.add_card, width=8).grid(row=0, column=0, padx=5)
        tk.Button(crud_frame, text="Edit", command=self.edit_card, width=8).grid(row=0, column=1, padx=5)
        tk.Button(crud_frame, text="Delete", command=self.delete_card, width=8).grid(row=0, column=2, padx=5)

        self.update_display()

    def update_display(self):
        if not self.flashcards:
            self.display.config(text="No flashcards available.")
            return

        card = self.flashcards[self.index]
        if self.show_answer:
            self.display.config(text=card["answer"])
        else:
            self.display.config(text=card["question"])

    def toggle_answer(self):
        self.show_answer = not self.show_answer
        self.update_display()

    def next_card(self):
        if self.flashcards:
            self.index = (self.index + 1) % len(self.flashcards)
            self.show_answer = False
            self.update_display()

    def prev_card(self):
        if self.flashcards:
            self.index = (self.index - 1) % len(self.flashcards)
            self.show_answer = False
            self.update_display()

    def add_card(self):
        q = simpledialog.askstring("Add Card", "Enter question:")
        a = simpledialog.askstring("Add Card", "Enter answer:")
        if q and a:
            self.flashcards.append({"question": q, "answer": a})
            messagebox.showinfo("Success", "Flashcard added!")
            self.index = len(self.flashcards) - 1
            self.update_display()

    def edit_card(self):
        if not self.flashcards:
            return
        q = simpledialog.askstring("Edit Card", "Update question:", initialvalue=self.flashcards[self.index]["question"])
        a = simpledialog.askstring("Edit Card", "Update answer:", initialvalue=self.flashcards[self.index]["answer"])
        if q and a:
            self.flashcards[self.index] = {"question": q, "answer": a}
            messagebox.showinfo("Success", "Flashcard updated!")
            self.update_display()

    def delete_card(self):
        if not self.flashcards:
            return
        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this card?")
        if confirm:
            self.flashcards.pop(self.index)
            if self.index >= len(self.flashcards):
                self.index = max(0, len(self.flashcards) - 1)
            self.update_display()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
