import os
import sys

b_d = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, b_d)

from dashbord.dashbord import *
from sabt.sabt import *
from dashbord.user_s import *
from search.search import*
def user_panel(e, c):
    for w in e.winfo_children():
        w.destroy()

    today = jdatetime.date.today().strftime("%Y/%m/%d")

    h = ctk.CTkFrame(e, fg_color="white", corner_radius=10)            
    h.pack(fill="x")

    date = ctk.CTkLabel(h, text=f"📅 {today}", text_color="#070707", font=("Arial", 13))
    date.pack(side="left", padx=10)

    ir = ctk.CTkLabel(h, text=f"👤 {c}", text_color="#2e2e2e", font=("Arial", 14))
    ir.pack(side="left", pady=15)

    r_lbl = ctk.CTkLabel(h, text="سامانه بسته‌های پستی | پست ایران    ", font=("Arial", 14), text_color="#e57a00")
    r_lbl.pack(side="right")

    rast = ctk.CTkFrame(e, width=200, height=500)
    rast.pack(side="right", fill="y", padx=5, pady=5)

    chap = ctk.CTkFrame(e, width=500, height=500)
    chap.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    bu2 = ctk.CTkButton(rast, text="ثبت بسته", width=110, fg_color="#e57a00", hover_color="#4f2523", corner_radius=20, command=lambda: show_sabt(chap))
    bu2.pack(pady=10)
    bu4 = ctk.CTkButton(rast, text="وضعیت بسته", width=110, fg_color="#e57a00", hover_color="#4f2523", corner_radius=20, command=lambda: aa(chap, c))
    bu4.pack(pady=10)
    exit = ctk.CTkButton(rast, text="خروج از برنامه", width=110, fg_color="red", command=e.quit)
    exit.pack(pady=10)


