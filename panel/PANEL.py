import os
import sys


b_d = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, b_d)
from sabt.im import *
from dashbord.dashbord import*
from sabt.sabt import*
from search.search import*
root = ctk.CTk()
root.geometry("700x500")

today = jdatetime.date.today().strftime("%Y/%m/%d")
h = ctk.CTkFrame(root, fg_color="white", corner_radius=10)
h.pack(fill="x")
lbl_date = ctk.CTkLabel(h, text=f"📅 {today}", text_color="#070707", font=("Arial", 13))
lbl_date.pack(side="left")

ir = ctk.CTkLabel(h, text="👤  سیستم", text_color="#2e2e2e", font=("Arial", 14))
ir.pack(side="left", pady=15)

r = ctk.CTkLabel(h, text="سامانه بسته‌های پستی | پست ایران    ", font=("Arial", 14), text_color="#e57a00")
r.pack(side="right")


paned = tk.PanedWindow(root, orient="horizontal", sashrelief="flat", bg="white")
paned.pack(fill="both", expand=True)

left = ctk.CTkFrame(paned, fg_color="#F2F3F1", width=580)
paned.add(left)
right = ctk.CTkFrame(paned, fg_color="#D7C15E", width=80)
paned.add(right)
bu1 = ctk.CTkButton(right, text="داشبورد", width=110, fg_color="#e57a00", hover_color="#4f2523", corner_radius=20,command=lambda: show_dashboard(left))
bu1.pack()


bu2 = ctk.CTkButton(right, text="ثبت بسته‌ها", width=110, fg_color="#e57a00", hover_color="#4f2523", corner_radius=20,command=lambda:show_sabt(left))
bu2.pack()
bu3 = ctk.CTkButton(right, text="لیست", width=110, fg_color="#e57a00", hover_color="#4f2523", corner_radius=20,command=lambda: ff(left))
bu3.pack()
root.mainloop()
