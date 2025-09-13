from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Function to translate text
def translate_text():
    try:
        src_lang = source_lang.get()
        tgt_lang = target_lang.get()
        text = input_text.get("1.0", END).strip()
        
        if text == "":
            messagebox.showwarning("Input Error", "Please enter some text to translate.")
            return
        
        translated = GoogleTranslator(source=src_lang, target=tgt_lang).translate(text)
        output_text.delete("1.0", END)
        output_text.insert(END, translated)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = Tk()
root.title("Language Translation Tool")
root.geometry("600x400")

Label(root, text="Enter Text:", font=("Arial", 12)).pack(anchor=W, padx=10, pady=5)
input_text = Text(root, height=5, width=70)
input_text.pack(padx=10)

# Dropdowns for languages
frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Source Lang:").grid(row=0, column=0, padx=5)
source_lang = ttk.Combobox(frame, values=["auto", "en", "hi", "fr", "es", "de"], width=10)
source_lang.set("auto")
source_lang.grid(row=0, column=1)

Label(frame, text="Target Lang:").grid(row=0, column=2, padx=5)
target_lang = ttk.Combobox(frame, values=["en", "hi", "fr", "es", "de"], width=10)
target_lang.set("hi")
target_lang.grid(row=0, column=3)

Button(frame, text="Translate", command=translate_text).grid(row=0, column=4, padx=10)

# Output box
Label(root, text="Translated Text:", font=("Arial", 12)).pack(anchor=W, padx=10, pady=5)
output_text = Text(root, height=5, width=70)
output_text.pack(padx=10)

root.mainloop()
