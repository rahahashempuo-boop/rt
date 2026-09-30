import os
import sys

b_d = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, b_d)
from sabt.im import *

tr = None
se = None


def do_search():
    matn = se.get().strip().lower()
    for row in tr.get_children():
        tr.delete(row)


    f = open("sabt/json.json", "r", encoding="utf-8")
    packages = json.load(f)
    f.close()

   
    for p in packages:
        name = str(p.get("receiver", "")).lower()
        code = str(p.get("code", "")).lower()

        if matn in name or matn in code:
            tr.insert("","end", values=(p.get("status", "-"),p.get("company", "-"),p.get("code", "-"),p.get("receiver", "-")))



def ff(t):
    global tr, se
    for w in t.winfo_children():
        w.destroy()
   
    s = ctk.CTkFrame(t, fg_color="transparent")
    s.pack(fill="x")

    bs = ctk.CTkButton(s,text="جستجو",width=70,height=30,fg_color="#EAA11F",hover_color="#D98E12",command=lambda:do_search())
    bs.pack(side="left", padx=5)

    se = ctk.CTkEntry(s,placeholder_text="جستجو نام یا کد...",width=200,height=30,justify="right",fg_color="#F3F4F6",text_color="#000000",border_color="#D1D5DB")
    se.pack(side="right")
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",font=("Arial", 10),background="white",foreground="#0A0909")
    style.configure("Treeview",font=("Arial", 9),background="white",fieldbackground="white")

    tr = ttk.Treeview(t, columns=("s", "cp", "c", "r"), show="headings")
    tr.heading("s", text="وضعیت")
    tr.heading("cp", text="شرکت حمل")
    tr.heading("c", text="کد رهگیری")
    tr.heading("r", text="نام گیرنده")

    for cl in ("s", "cp", "c", "r"):
        tr.column(cl, anchor="center", width=110)
    tr.pack(fill="both", expand=True)

    f = open("sabt/json.json", "r", encoding="utf-8")
    packages = json.load(f)
    f.close()

    for p in packages:
        tr.insert("","end",values=(p.get("status", "-"),p.get("company", "-"),p.get("code", "-"),p.get("receiver", "-")))
