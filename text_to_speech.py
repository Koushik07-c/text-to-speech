import pyttsx3
import tkinter as tk
from tkinter import filedialog, messagebox
from langdetect import detect
from gtts import gTTS
from playsound import playsound
import pyperclip
import PyPDF2
import os
import tempfile
import threading
import time

# Initialize pyttsx3 engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_dict = {
    f"{v.name} ({v.languages[0] if v.languages else 'Unknown'})": v.id
    for v in voices
}

# GUI Setup
root = tk.Tk()
root.title("AI Text-to-Speech App")
root.geometry("800x800")
root.configure(bg="#00B2B2")
root.minsize(800, 800)

# Fonts and Colors
FONT = ("Segoe UI", 11)
BTN_BG = "#00B2B2"
BTN_FG = "#000000"
TEXT_BG = "#E0FFFF"
TEXT_FG = "#000000"
ENTRY_BG = "#CCFFFF"
ENTRY_FG = "#000000"
HIGHLIGHT = "#009999"

# Hover Effects
def on_enter(e):
    e.widget['background'] = "#009999"
    e.widget['cursor'] = "hand2"

def on_leave(e):
    e.widget['background'] = BTN_BG

# Global flags
speak_thread = None
is_paused = False
is_stopped = False
current_index = 0
words = []

# Speak function
def speak_text_thread():
    global is_paused, is_stopped, current_index, words

    is_stopped = False
    is_paused = False

    while current_index < len(words):
        if is_stopped:
            break
        while is_paused:
            time.sleep(0.1)
        word = words[current_index]
        engine.say(word)
        engine.runAndWait()
        current_index += 1

def convert_text():
    global speak_thread, words, current_index, is_paused, is_stopped

    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Missing", "Please enter some text.")
        return

    engine.setProperty('voice', voice_dict[voice_var.get()])
    engine.setProperty('rate', speed_slider.get())

    words = text.split()
    current_index = 0
    is_paused = False
    is_stopped = False

    speak_thread = threading.Thread(target=speak_text_thread)
    speak_thread.start()

def pause_speech():
    global is_paused
    is_paused = True

def resume_speech():
    global is_paused
    is_paused = False

def stop_speech():
    global is_stopped, current_index
    is_stopped = True
    current_index = 0

# Multilingual
def speak_multilingual(text):
    try:
        lang = detect(text)
        tts = gTTS(text=text, lang=lang)
        temp_path = os.path.join(tempfile.gettempdir(), "temp_tts.mp3")
        tts.save(temp_path)
        playsound(temp_path)
        os.remove(temp_path)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def convert_multilingual():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Missing", "Please enter some text.")
        return
    speak_multilingual(text)

# File and clipboard
def read_clipboard():
    text_input.delete("1.0", tk.END)
    text_input.insert(tk.END, pyperclip.paste())

def open_text_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, content)

def open_pdf_file():
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if filepath:
        try:
            with open(filepath, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                content = ""
                for page in reader.pages:
                    content += page.extract_text()
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, content)
        except:
            messagebox.showerror("Error", "Could not read PDF.")

def save_audio():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Missing", "Please enter some text.")
        return
    filepath = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
    if filepath:
        tts = gTTS(text=text, lang=detect(text))
        tts.save(filepath)
        messagebox.showinfo("Success", f"Audio saved to {filepath}")

# UI Layout
text_input = tk.Text(root, height=15, width=70, wrap="word", font=FONT, bg=TEXT_BG, fg=TEXT_FG, insertbackground="white")
text_input.pack(pady=15)

controls_frame = tk.Frame(root, bg="#1e1e1e")
controls_frame.pack(pady=5)

voice_var = tk.StringVar()
voice_var.set(list(voice_dict.keys())[0])
voice_menu = tk.OptionMenu(controls_frame, voice_var, *voice_dict.keys())
voice_menu.config(font=FONT, bg=ENTRY_BG, fg=ENTRY_FG, highlightthickness=0)
voice_menu.pack(pady=5)

speed_slider = tk.Scale(controls_frame, from_=50, to=300, label="Speech Rate", orient="horizontal", bg="#1e1e1e", fg="white", troughcolor=HIGHLIGHT, font=FONT)
speed_slider.set(150)
speed_slider.pack(pady=5)

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

# Button builder
def create_button(text, command, row, col):
    b = tk.Button(btn_frame, text=text, command=command,
                  bg=BTN_BG, fg=BTN_FG, font=FONT,
                  height=3, width=20, relief="flat", bd=2, activebackground="#606060")
    b.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")
    b.bind("<Enter>", on_enter)
    b.bind("<Leave>", on_leave)
    return b

# Buttons
buttons = [
    ("Speak (Default)", convert_text),
    ("Speak (Multilingual)", convert_multilingual),
    ("Pause", pause_speech),
    ("Resume", resume_speech),
    ("Stop", stop_speech),
    ("Read from Clipboard", read_clipboard),
    ("Open Text File", open_text_file),
    ("Open PDF File", open_pdf_file),
    ("Save as MP3", save_audio)
]

for i, (text, command) in enumerate(buttons):
    create_button(text, command, i // 3, i % 3)

root.mainloop()
