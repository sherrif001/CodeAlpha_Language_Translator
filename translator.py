import tkinter as tk
from googletrans import Translator, LANGUAGES # type: ignore

translator = Translator()

def translate_text():
    text = entry.get()
    target_lang = lang_entry.get()

    try:
        translated = translator.translate(text, dest=target_lang)
        result_label.config(text=f"Translated: {translated.text}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def show_languages():
    """ Display available language abbreviations in a scrollable popup window """
    lang_window = tk.Toplevel(root)
    lang_window.title("Supported Languages")
    lang_window.geometry("250x300")  # Set window size

    frame = tk.Frame(lang_window)
    frame.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    lang_listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=40)
    for code in LANGUAGES:
        lang_listbox.insert(tk.END, f"{code}: {LANGUAGES[code]}")
    lang_listbox.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=lang_listbox.yview)

root = tk.Tk()
root.title("GoogleTrans Language Translator")

tk.Label(root, text="Enter text to translate:").pack()
entry = tk.Entry(root, width=40)
entry.pack()

tk.Label(root, text="Enter target language (e.g., 'es' for Spanish):").pack()
lang_entry = tk.Entry(root, width=10)
lang_entry.pack()

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

languages_button = tk.Button(root, text="Show Languages", command=show_languages)
languages_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()
 
tk.Label(root, text="Made by Sherif tamer").pack()
root.mainloop()
