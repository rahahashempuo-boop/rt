import os
import sys



b_d = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, b_d)
from sabt.im import *



def g():
    f = open("sabt/json.json", "r", encoding="utf-8")
    packages = json.load(f)
    f.close()
    total = len(packages)
    d = 0
    o = 0
    s = 0
    for p in packages:
        if p["status"] == "تحویل شده":
            d = d + 1
        if p["status"] == "در راه":
            o = o + 1
        if p["status"] == "ارسال شده":
            s = s + 1
    return total, d, o, s


def cr_c(p, v, t):
    card = ctk.CTkFrame(p, fg_color="white", width=120, height=80, corner_radius=6)
    card.pack(side="right", expand=True)
    card.pack_propagate(False)
    r = ctk.CTkLabel(card, text=str(v), font=("Arial", 16), text_color="black")
    r.pack()
    e = ctk.CTkLabel(card, text=t, font=("Arial", 13), text_color="#111111")
    e.pack()


def show_dashboard(l):
    for w in l.winfo_children():
        w.destroy()
    v, d, i, s = g()
    st_f = ctk.CTkFrame(l, fg_color="#FAF8F8")
    st_f.pack(fill="x", pady=20)

    cr_c(st_f, v, "📦 کل بسته‌ها")
    cr_c(st_f, d, "✅ تحویل شده")
    cr_c(st_f, i, "🚚 در راه")
    cr_c(st_f, s, "📤 ارسال شده")
    td = ctk.CTkFrame(l, fg_color="white", border_width=1, border_color="#E6F377")
    td.pack(fill="both", expand=True)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=("Arial", 10, ), background="white", foreground="#0A0909")
    style.configure("Treeview", font=("Arial", 9), background="white", fieldbackground="white")
    tr = ttk.Treeview(td, columns=("s", "cp", "c", "r"), show="headings")
    tr.heading("s", text="وضعیت")
    tr.heading("cp", text="شرکت حمل")
    tr.heading("c", text="کد رهگیری")
    tr.heading("r", text="نام گیرنده")

    for cl in ("s", "cp", "c", "r"):
        tr.column(cl, anchor="center", width=110)
    tr.pack(fill="both", expand=True, padx=10, pady=10)
    f = open("sabt/json.json", "r", encoding="utf-8")
    packages = json.load(f)
    f.close()

    for p in packages:
        tr.insert("", "end", values=(p.get("status", "-"),p.get("company", "-"),p.get("code", "-"), p.get("receiver", "-")))
