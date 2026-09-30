
import os
import sys
from users_panel import *
b_d = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, b_d)
from dashbord.dashbord import *
from sabt.im import *
from sabt.sabt import *
from sabt.sabt_user import*
from search.search import *

root = ctk.CTk()
root.geometry("700x500")
ent_user = None
ent_pass = None
def baz_kardan_panel():
    for w in root.winfo_children():
        w.destroy()
    today = jdatetime.date.today().strftime("%Y/%m/%d")
    h = ctk.CTkFrame(root, fg_color="white", corner_radius=10)
    h.pack(fill="x")
    date = ctk.CTkLabel(h, text=f"📅 {today}", text_color="#070707", font=("Arial", 13))
    date.pack(side="left", padx=10)
    ir = ctk.CTkLabel(h, text="👤  سیستم", text_color="#2e2e2e", font=("Arial", 14))
    ir.pack(side="left", pady=15)
    r = ctk.CTkLabel(h, text="سامانه بسته‌های پستی | پست ایران    ", font=("Arial", 14), text_color="#e57a00")
    r.pack(side="right")
    pa = tk.PanedWindow(root, orient="horizontal", sashrelief="flat", bg="white")
    pa.pack(fill="both", expand=True)
    left = ctk.CTkFrame(pa, fg_color="#2e2e2e", width=580)
    pa.add(left)
    right = ctk.CTkFrame(pa, fg_color="#252323", width=80)
    pa.add(right)
    bu1 = ctk.CTkButton(right, text="داشبورد", width=110, fg_color="#e57a00", hover_color="#4f2523", corner_radius=20, command=lambda: show_dashboard(left))
    bu1.pack(pady=10)
    bu2 = ctk.CTkButton(right, text="ثبت بسته‌ها", width=110, fg_color="#e57a00", hover_color="#4f2523", corner_radius=20, command=lambda: show_sabt(left))
    bu2.pack(pady=10)
    bu3 = ctk.CTkButton(right, text="لیست", width=110, fg_color="#e57a00", hover_color="#4f2523", corner_radius=20, command=lambda: ff(left))
    bu3.pack(pady=10)
    show_dashboard(left)


def barresi_admin():
    u = ent_user.get()
    p = ent_pass.get()
    f = open("panel/admin.json", "r", encoding="utf-8")
    admins = json.load(f)
    f.close()
    found = False
    if admins["username"] == u and admins["password"] == p:
        baz_kardan_panel()
    else:
        showerror("خطا", "اطلاعات ادمین اشتباه است")


def barresi_user():
    u = ent_user.get()
    o = ent_pass.get()
    f = open("panel/users.json", "r", encoding="utf-8")
    users = json.load(f)
    f.close()
    vojood_darad = False
    for item in users:
        if item["username"] == u and item["password"] == o:
            vojood_darad = True
        
    if vojood_darad == True:
        user_panel(root, ent_user.get())
    else:
        user_sabt(root)


ca = ctk.CTkFrame(root, fg_color="white", width=320, height=380, corner_radius=10, border_width=1, border_color="#D1D5DB")
ca.pack(expand=True)
ca.pack_propagate(False)
u=ctk.CTkLabel(ca, text="ورود به پنل", font=("Arial", 16), text_color="#e57a00")
u.pack(pady=15)
h=ctk.CTkLabel(ca, text=":نام کاربری", font=("Arial", 12), text_color="black")
h.pack(anchor="e", padx=30)
ent_user = ctk.CTkEntry(ca, width=250, justify="right")
ent_user.pack(pady=5)
e=ctk.CTkLabel(ca, text=":رمز عبور", font=("Arial", 12), text_color="black")
e.pack(anchor="e", padx=30)
ent_pass = ctk.CTkEntry(ca, width=250, justify="right", show="*")
ent_pass.pack(pady=5)
btn_admin = ctk.CTkButton(ca, text="ادمین هستم", fg_color="#e57a00", hover_color="#4f2523", command=lambda:barresi_admin())
btn_admin.pack(pady=8)
btn_user = ctk.CTkButton(ca, text="یوزر هستم", fg_color="#e57a00", hover_color="#4f2523", command=lambda:barresi_user())
btn_user.pack(pady=8)
b = ctk.CTkButton(ca, text="خروج", fg_color="#ff0d0d", command=lambda:root.destroy())
b.pack(pady=8)
root.mainloop()
