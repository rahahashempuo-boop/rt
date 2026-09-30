import os
import sys
import json
import customtkinter as ctk

def aa(dd, username):
    for widget in dd.winfo_children():
        widget.destroy()

    f = open("sabt/json.json", "r", encoding="utf-8")
    packages = json.load(f)
    f.close()

    peida_shod = False

    for p in packages:
        if str(p.get("receiver", "")).strip() == str(username).strip():
            peida_shod = True
            card = ctk.CTkFrame(dd)
            card.pack(pady=5, padx=10, fill="x")
            ctk.CTkLabel(card, text=f"گیرنده: {p.get('receiver', '')}").pack(pady=2)
            ctk.CTkLabel(card, text=f"کد رهگیری: {p.get('code', '')}").pack(pady=2)
            ctk.CTkLabel(card, text=f"وضعیت: {p.get('status', '')}").pack(pady=2)

    if not peida_shod:
        ctk.CTkLabel(dd, text=f"هیچ بسته‌ای برای ({username}) یافت نشد!", text_color="red", font=("Arial", 14)).pack(pady=20)
