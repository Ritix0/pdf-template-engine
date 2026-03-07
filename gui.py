import os, sys, io, json, importlib, base64
from datetime import datetime
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
from core.pdf_engine import PDFEngine

def _v(s): return base64.b64decode(s).decode()
_gx = importlib.import_module(_v('cXJjb2Rl'))

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

if getattr(sys, 'frozen', False): B_D = os.path.dirname(sys.executable)
else: B_D = os.path.dirname(os.path.abspath(__file__))

if B_D not in sys.path: sys.path.append(B_D)

class PApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.p22()
        self.c = self.p3()
        self.title(self.p4("n_1", "App"))
        self.geometry("1150x950")
        self.p5()
        self.s_f = os.path.join(B_D, "settings.json")
        self.o_p = self.p10()
        self.tmpls = self.p6()
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.sb = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sb.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(self.sb, text=self.p4("n_2"), font=ctk.CTkFont(size=20, weight="bold")).pack(padx=20, pady=(20, 10))
        ctk.CTkButton(self.sb, text=self.p4("n_10"), height=24, fg_color="transparent", border_width=1,command=self.p23).pack(padx=20, pady=(0, 10))
        ctk.CTkLabel(self.sb, text=self.p4("n_3")).pack(padx=20, pady=(10, 0))
        nms = list(self.tmpls.keys())
        self.t_o = ctk.CTkOptionMenu(self.sb, values=nms if nms else [self.p4("n_9")], command=self.p7)
        self.t_o.pack(padx=20, pady=10)
        ctk.CTkLabel(self.sb, text=self.p4("n_4"), font=ctk.CTkFont(size=12)).pack(padx=20, pady=(20, 0))
        self.p_d = ctk.CTkLabel(self.sb, text=self.p11(self.o_p), text_color="gray")
        self.p_d.pack(padx=20, pady=5)
        ctk.CTkButton(self.sb, text=self.p4("n_5"), command=self.p9).pack(padx=20, pady=10)
        ctk.CTkButton(self.sb, text=self.p4("n_6"), fg_color="transparent", border_width=1, command=self.p14).pack(padx=20, pady=10)
        ctk.CTkButton(self.sb, text=self.p4("n_7"), fg_color="green", hover_color="#006400", command=self.p1).pack(side="bottom", padx=20, pady=20)
        self.scr = ctk.CTkScrollableFrame(self, label_text=self.p4("n_8"))
        self.scr.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.scr.grid_columnconfigure((0, 1, 2), weight=1)
        self.p2()
        self.bind_all("<KeyPress>", self.p8, add="+")

    def p22(self):
        a_f = os.path.join(B_D, ".accepted")
        if os.path.exists(a_f): return
        top = ctk.CTkToplevel(self)
        top.title("Пользовательское соглашение")
        top.geometry("600x500")
        top.protocol("WM_DELETE_WINDOW", sys.exit)
        top.attributes("-topmost", True)
        
        txt = (
            "ЛИЦЕНЗИОННОЕ СОГЛАШЕНИЕ И ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ (EULA)\n"
            "----------------------------------------------------------\n\n"
            "1. ОПРЕДЕЛЕНИЯ:\n"
            "1.1. РАЗРАБОТЧИК — автор исходного кода программы, размещенного на платформе GitHub.\n"
            "1.2. ПОЛЬЗОВАТЕЛЬ — любое физическое или юридическое лицо, осуществившее "
            "запуск, копирование или модификацию данной программы.\n"
            "1.3. ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ (ПО) — технический движок для автоматизации "
            "заполнения PDF-файлов по заданным координатам.\n\n"
            
            "2. ПРЕДМЕТ СОГЛАШЕНИЯ:\n"
            "2.1. Данное ПО является техническим инструментом (фреймворком) и поставляется «КАК ЕСТЬ» (AS IS).\n"
            "2.2. Программа НЕ СОДЕРЖИТ встроенных шаблонов документов, бланков строгой отчетности или "
            "инструментов для обхода систем защиты.\n\n"
            
            "3. РАЗГРАНИЧЕНИЕ ОТВЕТСТВЕННОСТИ:\n"
            "3.1. Разработчик НЕ НЕСЕТ ответственности за характер документов, создаваемых Пользователем. "
            "Все шаблоны (.pdf) и скрипты координат (.py) создаются Пользователем самостоятельно.\n"
            "3.2. Пользователь подтверждает, что обладает законным правом на редактирование и использование "
            "загружаемых в программу исходных PDF-файлов.\n"
            "3.3. Разработчик не несет ответственности за любые прямые или косвенные убытки, "
            "упущенную выгоду или юридические последствия, возникшие в результате использования ПО.\n\n"
            
            "4. ЗАПРЕЩЕННОЕ ИСПОЛЬЗОВАНИЕ:\n"
            "Пользователю КАТЕГОРИЧЕСКИ ЗАПРЕЩАЕТСЯ использовать ПО для:\n"
            "- Создания поддельных документов, удостоверений, справок или финансовых чеков;\n"
            "- Введения в заблуждение государственных органов или коммерческих организаций;\n"
            "- Любой иной деятельности, нарушающей Уголовный кодекс или иные законы вашей страны.\n\n"
            
            "5. СОГЛАСИЕ:\n"
            "Нажимая кнопку 'Принимаю', вы подтверждаете, что являетесь полностью дееспособным лицом, "
            "осознаете техническую суть программы и принимаете на себя ПОЛНУЮ единоличную ответственность "
            "за любые действия, совершенные с помощью данного инструмента.\n\n"
            "Если вы не согласны с данными условиями, вы обязаны немедленно прекратить "
            "использование программы и удалить ее исходный код."
        )

        label = ctk.CTkTextbox(top, width=560, height=350)
        label.insert("0.0", txt)
        label.configure(state="disabled")
        label.pack(padx=20, pady=20)

        def accept():
            with open(a_f, "w") as f: f.write("accepted")
            top.destroy()

        btn_f = ctk.CTkFrame(top, fg_color="transparent")
        btn_f.pack(fill="x", padx=20, pady=(0, 20))

        ctk.CTkButton(btn_f, text="Выход", fg_color="red", command=sys.exit).pack(side="left", padx=10)
        ctk.CTkButton(btn_f, text="Принимаю", fg_color="green", command=accept).pack(side="right", padx=10)

        top.grab_set()

    def p23(self):
        top = ctk.CTkToplevel(self)
        top.title(self.p4("n_10"))
        top.geometry("450x350")
        top.attributes("-topmost", True)
        top.resizable(False, False)

        ctk.CTkLabel(top, text="PDF Engine App", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=(20, 5))
        ctk.CTkLabel(top, text="Версия 1.0.0 (Open Source Edition)", font=ctk.CTkFont(size=12)).pack(pady=0)

        info_txt = (
            "Универсальный инструмент для автоматизации заполнения\n"
            "PDF-документов на основе пользовательских шаблонов.\n\n"
            "Разработано для GitHub портфолио.\n"
            "Технологии: Python, CustomTkinter, PyMuPDF.\n\n"
            "Данное ПО является свободным. Вы можете использовать,\n"
            "изучать и модифицировать его в рамках лицензии MIT."
        )
        ctk.CTkLabel(top, text=info_txt, justify="center").pack(pady=20)

        ctk.CTkButton(top, text="Прочитать соглашение", fg_color="gray", height=28,
                      command=lambda: [top.destroy(), self.p22_force()]).pack(pady=5)

        ctk.CTkButton(top, text="Закрыть", command=top.destroy).pack(pady=(20, 10))

    def p22_force(self):
        a_f = os.path.join(B_D, ".accepted")
        if os.path.exists(a_f): os.remove(a_f)
        self.p22()

    def p3(self):
        p = os.path.join(B_D, "ui_config.json")
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f: return json.load(f)
            except: return {}
        return {}

    def p4(self, k, d=""): return self.c.get(k, d)

    def p5(self):
        for f in [self.p4("sys_p_1"), self.p4("sys_p_2"), self.p4("sys_p_3")]:
            p = os.path.join(B_D, f)
            if not os.path.exists(p): os.makedirs(p)

    def p6(self):
        d = os.path.join(B_D, self.p4("sys_p_1")); fnd = {}
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.endswith(".py") and f != "__init__.py":
                    n = f[:-3]; fnd[n] = f"{self.p4('sys_p_1')}.{n}"
        return fnd
    
    def p7(self, _=None):
        tn = self.t_o.get()
        if tn == self.p4("n_9"): return
        try:
            mp = self.tmpls[tn]; tm = importlib.import_module(mp); importlib.reload(tm)
            rf, rv = getattr(tm, self.p4("tm_k_1"), {}), getattr(tm, self.p4("tm_k_11"), {})
            pref, c = self.p4("pre_1"), 0
            while f"{pref}_{c + 1}" in rf or f"{pref}_{c + 1}" in rv: c += 1
            for i, e in enumerate(self.d_i):
                if i < c: e.grid(row=i+1, column=0, columnspan=3, padx=10, pady=5, sticky="ew")
                else: e.grid_forget()
        except: pass
        
    def p8(self, ev):
        if ev.state & 4:
            f = self.focus_get()
            if not f or not hasattr(f, 'event_generate'): return
            tr = f._entry if hasattr(f, '_entry') else f
            if ev.keycode == 86: tr.event_generate("<<Paste>>"); return "break"
            elif ev.keycode == 67: tr.event_generate("<<Copy>>"); return "break"
            elif ev.keycode == 88: tr.event_generate("<<Cut>>"); return "break"
            elif ev.keycode == 65:
                try: tr.select_range(0, 'end'); tr.icursor('end')
                except: pass
                return "break"

    def p2(self):
        s1 = self.p15(self.p4("s_1"), 0)
        self.e_1 = self.p16(s1, self.p4("l_1"), self.p4("d_1"), 0, 0)
        self.e_2 = self.p16(s1, self.p4("l_2"), self.p4("d_2"), 0, 1)
        self.e_3 = self.p16(s1, self.p4("l_3"), self.p4("d_3"), 1, 0, 2)
        self.e_4 = self.p16(s1, self.p4("l_4"), self.p4("d_4"), 2, 0, 2)
        s2 = self.p15(self.p4("s_2"), 1)
        self.e_5 = self.p16(s2, self.p4("l_5"), self.p4("d_5"), 0, 0, 3)
        self.e_6 = self.p16(s2, self.p4("l_6"), "", 1, 0, 2)
        self.ch_1 = ctk.CTkCheckBox(s2, text=self.p4("c_1"), command=self.p18); self.ch_1.grid(row=3, column=2, padx=10, pady=(0, 10), sticky="w")
        s3 = self.p15(self.p4("s_3"), 2)
        self.e_7 = self.p16(s3, self.p4("l_7"), self.p4("d_7"), 0, 0)
        self.e_8 = self.p16(s3, self.p4("l_8"), self.p4("d_8"), 0, 1)
        self.e_9 = self.p16(s3, self.p4("l_9"), self.p4("d_9"), 0, 2)
        ctk.CTkLabel(s3, text=self.p4("l_10")).grid(row=2, column=0, padx=10, pady=(5, 0), sticky="w")
        self.o_1 = ctk.CTkOptionMenu(s3, values=self.p4("list_1", ["-"])); self.o_1.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="ew")
        self.e_10 = self.p16(s3, self.p4("l_11"), self.p4("d_11"), 1, 1)
        self.e_11 = self.p16(s3, self.p4("l_12"), self.p4("d_12"), 1, 2)
        ctk.CTkLabel(s3, text=self.p4("l_13")).grid(row=4, column=0, padx=10, pady=(5, 0), sticky="w")
        self.o_2 = ctk.CTkOptionMenu(s3, values=self.p4("list_2", ["-"])); self.o_2.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="ew")
        self.ch_2 = ctk.CTkCheckBox(s3, text=self.p4("c_2")); self.ch_2.grid(row=5, column=1, padx=10, pady=(0, 10), sticky="w")
        s4 = self.p15(self.p4("s_4"), 3)
        self.ch_3 = ctk.CTkCheckBox(s4, text=self.p4("c_3"), command=self.p19); self.ch_3.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.d_i = []
        pt = self.p4("p_1", "{idx}")
        for i in range(10):
            e = ctk.CTkEntry(s4, placeholder_text=pt.format(idx=i+1), width=650); self.d_i.append(e)
        self.p7()
        s5 = self.p15(self.p4("s_5"), 4)
        self.cf = {}
        ks, ls, ds = self.p4("k_c", []), self.p4("l_c", {}), self.p4("d_c", {})
        for i, k in enumerate(ks):
            e = self.p16(s5, ls.get(k, k), ds.get(k, "1"), i // 5, i % 5); self.cf[k] = e
        self.e_12 = self.p16(s5, self.p4("l_14"), self.p4("d_14"), 2, 0, 2)

    def p10(self):
        p = os.path.join(B_D, "settings.json")
        if os.path.exists(p):
            try:
                with open(p, "r") as f: return json.load(f).get("output_path", os.path.join(B_D, "output"))
            except: pass
        return os.path.join(B_D, "output")

    def p9(self):
        np = filedialog.askdirectory(initialdir=self.o_p)
        if np: self.o_p = np; self.p_d.configure(text=self.p11(self.o_p)); self.p20()

    def p11(self, p): return "..." + p[-22:] if len(p) > 25 else p

    def p14(self):
        if os.path.exists(self.o_p): os.startfile(self.o_p)

    def p15(self, t, r):
        f = ctk.CTkFrame(self.scr); f.grid(row=r, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(f, text=t, font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="w")
        in_f = ctk.CTkFrame(f, fg_color="transparent"); in_f.grid(row=1, column=0, columnspan=3, sticky="nsew"); return in_f

    def p12(self, ev):
        try: self.scr._parent_canvas.yview_scroll(int(-1 * (ev.delta / 120) * 10), "units")
        except: pass

    def p16(self, p, l, pl, r=0, c=0, cs=1):
        ctk.CTkLabel(p, text=l).grid(row=r*2, column=c, padx=10, pady=(5, 0), sticky="w")
        e = ctk.CTkEntry(p, placeholder_text=pl); e.grid(row=r*2+1, column=c, columnspan=cs, padx=10, pady=(0, 10), sticky="ew")
        if pl: e.insert(0, pl)
        in_e = e._entry if hasattr(e, '_entry') else e; in_e.bind("<MouseWheel>", self.p12); self.p17(e); return e

    def p17(self, w):
        i = w._entry if hasattr(w, '_entry') else w; m = tk.Menu(self, tearoff=0)
        m.add_command(label=self.p4("m_1"), command=lambda: i.event_generate("<<Cut>>"))
        m.add_command(label=self.p4("m_2"), command=lambda: i.event_generate("<<Copy>>"))
        m.add_command(label=self.p4("m_3"), command=lambda: i.event_generate("<<Paste>>"))
        m.add_separator(); m.add_command(label=self.p4("m_4"), command=lambda: i.select_range(0, 'end'))
        i.bind("<Button-3>", lambda e: m.tk_popup(e.x_root, e.y_root))

    def p18(self):
        if self.ch_1.get(): self.e_6.delete(0, "end"); self.e_6.insert(0, self.e_5.get())

    def p19(self):
        s = "normal" if self.ch_3.get() else "disabled"
        for e in self.d_i: e.configure(state=s)

    def p20(self):
        with open(self.s_f, "w") as f: json.dump({"output_path": self.o_p}, f)

    def p21(self, r, s, e, d):
        dg = "".join([c for c in r if c.isdigit()])
        if len(dg) == 12:
            for i in range(6): d[f"{s}_{i+1}"] = dg[i]; d[f"{e}_{i+1}"] = dg[6+i]

    def p1(self):
        tn = self.t_o.get()
        if tn == self.p4("x_9"): return
        try:
            mp = self.tmpls[tn]; tm = importlib.import_module(mp); importlib.reload(tm)
            rf, inf, fs = getattr(tm, self.p4("tm_k_1")), getattr(tm, self.p4("tm_k_2")), getattr(tm, self.p4("tm_k_3"), {})
            c_on, c_off = getattr(tm, self.p4("tm_k_4"), "X"), getattr(tm, self.p4("tm_k_5"), "")
        except Exception as ex: messagebox.showerror(self.p4("msg_e"), f"{self.p4('msg_t')}\n{str(ex)}"); return

        v_m = self.e_5.get().strip(); dm = self.p4("map", {}); d_k = self.p4("d_k", {})
        if not v_m: messagebox.showwarning(self.p4("msg_w"), self.p4("msg_f")); return

        dt = {
            dm["f_1"]: v_m, dm["f_2"]: v_m, dm["f_3"]: self.e_6.get() or v_m,
            dm["f_4"]: self.e_7.get().upper(), dm["f_5"]: self.e_8.get().upper(),
            dm["f_6"]: self.e_9.get().upper(), dm["f_7"]: self.o_1.get(),
            dm["f_8"]: self.e_10.get().upper(), dm["f_9"]: self.e_11.get(),
            dm["f_10"]: self.e_1.get().upper(), dm["f_11"]: self.e_2.get(),
        }
        if getattr(tm, self.p4("tm_k_6"), False):
            dt[dm["f_1"]] = v_m.upper(); dt[dm["f_3"]] = dt[dm["f_3"]].upper()
        if getattr(tm, self.p4("tm_k_7"), False):
            p = v_m.split(); dt[f"{dm['f_1']}_1"] = " ".join(p[:2]) if len(p) >= 2 else v_m
            dt[f"{dm['f_1']}_2"] = " ".join(p[2:]) if len(p) >= 3 else ""

        _o = getattr(_gx, _v('UVJDb2Rl'))(version=None, error_correction=getattr(getattr(_gx, _v('Y29uc3RhbnRz')), _v('RVJST1JfQ09SUkVDVF9I')), box_size=20, border=0)
        _o.add_data(self.p4("pre_5").format(number=dt[dm["f_11"]])); _o.make(fit=True)
        _im = _o.make_image(fill_color="black", back_color="white"); _b = io.BytesIO(); _im.save(_b, format='PNG'); dt[dm["f_13"]] = _b.getvalue()

        nw = datetime.now(); mf = getattr(tm, self.p4("tm_k_8"), "word")
        if mf == self.p4("log_f_1"): m = f"{nw.month:02d}"
        else:
            m = {i+1: month for i, month in enumerate(self.p4("months_ru", []))}.get(nw.month, "01")
        d, fy, ys = f"{nw.day:02d}", str(nw.year), (self.p4("log_f_3") if getattr(tm, self.p4("tm_k_9"), False) else "")
        dv, y = (f"«{d}»" if getattr(tm, self.p4("tm_k_10"), False) else d), fy[2:]
        dt.update({
            d_k["k1"]: dv, d_k["k2"]: m, d_k["k3"]: y, d_k["k4"]: dv, d_k["k5"]: m, d_k["k6"]: y,
            d_k["k7"]: fy[0], d_k["k8"]: fy[1], d_k["k9"]: fy[2], d_k["k10"]: fy[3] + ys,
            d_k["k11"]: fy[0], d_k["k12"]: fy[1], d_k["k13"]: fy[2], d_k["k14"]: fy[3] + ys,
        })
        if mf == self.p4("log_f_1"):
            dt.update({
                d_k["k15"]: d[0], d_k["k16"]: d[1], d_k["k17"]: m[0], d_k["k18"]: m[1], d_k["k27"]: y[0], d_k["k28"]: y[1],
                d_k["k19"]: d[0], d_k["k20"]: d[1], d_k["k21"]: m[0], d_k["k22"]: m[1], d_k["k23"]: d[0], d_k["k24"]: d[1]
            })
        dt.update({d_k["k25"]: f"{nw.month:02d}"[0], d_k["k26"]: f"{nw.month:02d}"[1], d_k["k27"]: y[0], d_k["k28"]: y[1]})
        for k, e in self.cf.items(): dt[f"{self.p4('pre_4')}{k}"] = e.get()

        uks, uvs = self.p4("u_k", []), self.p4("list_2", [])
        for pk in uks: dt[pk] = c_off
        try:
            idx = uvs.index(self.o_2.get())
            if idx < len(uks): dt[uks[idx]] = c_on
        except: 
            if uks: dt[uks[0]] = c_on

        rp, dp, vp = self.p4("pre_1"), self.p4("pre_2"), self.p4("pre_3")
        cr = {k: v for k, v in rf.items() if not k.startswith(rp)}; all_v = getattr(tm, self.p4("tm_k_11"), {})
        c_on_r, c_off_r = getattr(tm, "CHAR_RESTRICTED_ON", c_on), getattr(tm, "CHAR_RESTRICTED_OFF", c_off)

        if self.ch_3.get():
            dt[dm["f_14"]], dt[dm["f_15"]] = c_on_r, c_off_r
            for i, e in enumerate(self.d_i):
                idx, ds = i + 1, e.get().strip()
                if ds:
                    p = ds.split()
                    if len(p) >= 4:
                        dt[f"{dp}_{idx}{self.p4('sfx_1')}"] = " ".join(p[:-3])
                        dt[f"{dp}_{idx}{self.p4('sfx_2')}"] = f"{p[-3]} {p[-2]}"
                        dt[f"{dp}_{idx}{self.p4('sfx_3')}"] = p[-1]
                        dt[f"{dp}_{idx}{self.p4('sfx_4')}"] = str(idx)
                    if f"{rp}_{idx}" in rf: cr[f"{rp}_{idx}"] = rf[f"{rp}_{idx}"]
                    if f"{rp}_{idx}" in all_v: cr[f"{vp}_{idx}"] = all_v[f"{rp}_{idx}"]
        else: dt[dm["f_14"]], dt[dm["f_15"]] = c_off_r, c_on_r

        try: dt[dm["f_12"]] = float(self.e_12.get().replace(" ", "").replace(",", "."))
        except: dt[dm["f_12"]] = 0.0
        dt[dm["f_16"]], dt[dm["f_17"]] = (c_on, c_off) if self.ch_2.get() else (c_off, c_on)
        
        self.p21(self.e_3.get(), self.p4("map")["f_19"], self.p4("map")["f_20"], dt)
        self.p21(self.e_4.get(), self.p4("map")["f_21"], self.p4("map")["f_22"], dt)

        fn = v_m.replace(" ", "_") + ".pdf"; op, ip = os.path.join(self.o_p, fn), os.path.join(B_D, self.p4("sys_p_2"), f"{tn}.pdf")
        if not os.path.exists(ip): messagebox.showerror(self.p4("msg_e"), self.p4("msg_p").format(path=ip)); return
        if not os.path.exists(self.o_p): os.makedirs(self.o_p)
        try:
            PDFEngine(cr, inf, fs, self.c).fill_pdf(ip, op, dt); os.startfile(op)
        except PermissionError: messagebox.showerror(self.p4("msg_a"), self.p4("msg_c").format(file=fn))
        except Exception as ex: messagebox.showerror(self.p4("msg_e"), str(ex))

if __name__ == "__main__":
    app = PApp(); app.mainloop()