import os
import sys

from tkinter import *
b_d = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, b_d)
from sabt.im import *


name = None
code = None
c3 = None
cs = None

import json
import re


def save_data():
    name2 = name.get().strip()
    code2 = code.get().strip()
    co2 = c3.get()
    ss2 = cs.get()

    if name2 == "" or code2 == "":
        showerror("خطا", "لطفاً تمام فیلدها را پر کنید")
        return

    olgoo = r"^[a-zA-Z0-9]{13,}$"
    if not re.match(olgoo, code2):
        showerror("خطا", "کد رهگیری باید حداقل ۱۳ رقم و فقط شامل حروف و عدد باشد")
        return

    f = open("sabt/json.json", "r", encoding="utf-8")
    packages = json.load(f)
    f.close()

    new = {"receiver": name2, "code": code2, "company": co2, "status": ss2}
    packages.append(new)

    f = open("panel/json.json", "w", encoding="utf-8")
    json.dump(packages, f, ensure_ascii=False)
    f.close()
    showinfo("موفق", "بسته با موفقیت ثبت شد")
    name.delete(0, "end")
    code.delete(0, "end")



def show_sabt(t):
    global name, code, c3, cs
    for w in t.winfo_children():
        w.destroy()

    card = ctk.CTkFrame(t, fg_color="white", width=340, height=420, corner_radius=8, border_width=1, border_color="#D1D5DB")
    card.pack(expand=True, pady=20)
    card.pack_propagate(False)
    title = ctk.CTkLabel(card, text="فرم ثبت بسته جدید", font=("Arial", 15), text_color="#040404")
    title.pack(pady=10)

    l1 = ctk.CTkLabel(card, text=":نام گیرنده", font=("Arial", 11), text_color="#000000")
    l1.pack(anchor="e", padx=35)
    name = ctk.CTkEntry(card, width=270, height=32, justify="right",fg_color="#F3F4F6",text_color="#000000",border_color="#D1D5DB")
    name.pack()
    l2 = ctk.CTkLabel(card, text=":کد رهگیری", font=("Arial", 11), text_color="#000000")
    l2.pack(anchor="e", padx=35)
    code = ctk.CTkEntry(card, width=270, height=32, justify="right",fg_color="#F3F4F6",text_color="#000000",border_color="#D1D5DB")
    code.pack()

    l3 = ctk.CTkLabel(card, text=":شرکت حمل", font=("Arial", 11), text_color="#000000")
    l3.pack(anchor="e", padx=35)
    c3 = ctk.CTkOptionMenu(card, values=["پست پیشتاز", "تیپاکس", "پست سفارشی", "چاپار"], width=270, height=32,  fg_color="#F3F4F6",button_color="#EAA11F",button_hover_color="#D98E12",text_color="#000000",dropdown_fg_color="white",dropdown_text_color="black")
    c3.set("پست پیشتاز")
    c3.pack()
    l4 = ctk.CTkLabel(card, text=":وضعیت اولیه", font=("Arial", 11), text_color="#000000")
    l4.pack(anchor="e", padx=35)
    cs = ctk.CTkOptionMenu(card, values=["ارسال شده", "در راه", "تحویل شده"], width=270, height=32,  fg_color="#F3F4F6",button_color="#EAA11F",button_hover_color="#D98E12",text_color="#000000",dropdown_fg_color="white",dropdown_text_color="black")
    cs.set("ارسال شده")
    cs.pack()
    btn_save = ctk.CTkButton(card, text="ثبت و ذخیره", font=("Arial", 12), fg_color="#EAA11F", hover_color="#D98E12", width=130, height=35, command=lambda:save_data())
    btn_save.pack(pady=15)