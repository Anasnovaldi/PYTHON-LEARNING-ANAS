import tkinter as tk
from tkinter import ttk
import random

window = tk.Tk()
window.configure(bg="black")
window.geometry("380x200")
window.resizable(False, False)
window.title("🎮 SUIT MANIA 🎮") 


OPTIONS = {
    "BATU": "✊ BATU",
    "GUNTING": "✌️ GUNTING",
    "KERTAS": "🖐️ KERTAS"
}

PILIHAN_BOT = random.choice(list(OPTIONS.keys()))
PILIHAN_USER = tk.StringVar()

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="black", foreground="white", font=("Arial", 12, "bold"))
style.configure("TButton", background="white", foreground="black", font=("Arial", 11, "bold"))
style.configure("TCombobox", fieldbackground="black", background="white", foreground="white")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)


def tombol_click():
    for widget in input_frame.winfo_children():
        widget.destroy()
    
    hasil_label = ttk.Label(input_frame, text="📢 HASIL SUIT:", font=("Arial", 13, "bold"))
    hasil_label.pack(pady=5)

    if PILIHAN_USER.get() == PILIHAN_BOT:
        hasil_entry = ttk.Label(input_frame,
            text=f"🤝 SERI! Bot juga pilih {OPTIONS[PILIHAN_BOT]}")
        hasil_entry.pack(pady=10)

    elif (PILIHAN_USER.get() == "BATU" and PILIHAN_BOT == "GUNTING") or \
         (PILIHAN_USER.get() == "GUNTING" and PILIHAN_BOT == "KERTAS") or \
         (PILIHAN_USER.get() == "KERTAS" and PILIHAN_BOT == "BATU"):
        hasil_entry = ttk.Label(input_frame,
            text=f"🏆 ANDA MENANG! Bot pilih {OPTIONS[PILIHAN_BOT]}")
        hasil_entry.pack(pady=10)
    else:
        hasil_entry = ttk.Label(input_frame,
            text=f"😢 ANDA KALAH! Bot pilih {OPTIONS[PILIHAN_BOT]}")
        hasil_entry.pack(pady=10)

    # Tombol main lagi
    ulang_btn = ttk.Button(input_frame, text="🔄 Main Lagi", command=reset_game)
    ulang_btn.pack(pady=10, fill="x")

def reset_game():
    global PILIHAN_BOT
    PILIHAN_BOT = random.choice(list(OPTIONS.keys()))
    for widget in input_frame.winfo_children():
        widget.destroy()
    setup_ui()

def setup_ui():
    mode_label = ttk.Label(input_frame, text="👉 Pilih SUIT Anda:", font=("Arial", 12, "bold"))
    mode_label.pack(fill="x", pady=5)

    mode_box = ttk.Combobox(input_frame, textvariable=PILIHAN_USER,
                            values=list(OPTIONS.keys()), state="readonly")
    mode_box.pack(fill="x", pady=5)

    tombol_pilih = ttk.Button(input_frame, text="✅ PILIH", command=tombol_click)
    tombol_pilih.pack(fill='x', expand=True, padx=10, pady=10)

setup_ui()
window.mainloop()