import os
import sys
import json
import re
from tkinter.messagebox import showerror, showinfo
import customtkinter as ctk

b_d = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, b_d)
from sabt.im import *
from panel.users_panel import *

name = None
code = None
c3 = None

def save_data(t):
    global name, code, c3
    n = name.get().strip()
    c = code.get().strip()
    co = c3.get()

    if n == "" or c == "":
        showerror("خطا", "همه فیلدها را پر کنید")
        return

    if not re.match(r"[a-zA-Z0-9]{13}", c):
        showerror("خطا", "کد باید حداقل ۱۳ کاراکتر باشد")
        return

    json_path = os.path.join(b_d, "sabt/json.json")
    
    f = open(json_path, "r", encoding="utf-8")
    packages = json.load(f)
    f.close()

    packages.append({"receiver": n, "code": c, "company": co, "status": "در حال پردازش"})

    f = open(json_path, "w", encoding="utf-8")
    json.dump(packages, f, ensure_ascii=False, indent=4)
    f.close()

    showinfo("موفق", "ثبت با موفقیت انجام شد")
    user_panel(t,n)

def user_sabt(t):
    global name, code, c3
    for w in t.winfo_children():
        w.destroy()

    card = ctk.CTkFrame(t, fg_color="white", width=340, height=380)
    card.pack(expand=True, pady=20)
    card.pack_propagate(False)

    ctk.CTkLabel(card, text="فرم ثبت بسته جدید", text_color="black").pack(pady=10)

    name = ctk.CTkEntry(card, width=270, placeholder_text="نام گیرنده")
    name.pack(pady=5)

    code = ctk.CTkEntry(card, width=270, placeholder_text="کد رهگیری")
    code.pack(pady=5)

    c3 = ctk.CTkComboBox(card, values=["پست پیشتاز", "تیپاکس", "اسنپ باکس"], width=270)
    c3.pack(pady=5)

    o=ctk.CTkButton(card, text="ثبت و ذخیره", fg_color="#EAA11F", command=lambda: save_data(t))
    o.pack(pady=20)
