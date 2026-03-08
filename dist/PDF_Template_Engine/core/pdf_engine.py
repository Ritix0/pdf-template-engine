import importlib, os, sys, base64

def _v(s): return base64.b64decode(s).decode()
_m = importlib.import_module(_v('Zml0eg=='))

if getattr(sys, 'frozen', False): 
    B_D = os.path.dirname(sys.executable)
else: 
    B_D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class PDFEngine:
    def __init__(self, r, i, s, c):
        self.r, self.i, self.s, self.c = r, i, s, c
        self._rt = getattr(_m, _v('UmVjdA=='))

    def _gb(self, l):
        return self._rt(min(x[0] for x in l), min(x[1] for x in l), max(x[2] for x in l), max(x[3] for x in l)) if l else None

    def _gs(self, k):
        t = self.s.get(self.c.get("pe_1"), {
            self.c.get("pe_2"): self.c.get("pe_3"),
            self.c.get("pe_4"): 10, self.c.get("pe_5"): (0,0,0), self.c.get("pe_6"): 0
        }).copy()
        if k in self.s: t.update(self.s[k]); return t
        for x in sorted([y for y in self.s.keys() if y != self.c.get("pe_1")], key=len, reverse=True):
            if x in k: t.update(self.s[x]); break
        return t

    def fill_pdf(self, ip, op, d):
        dc = getattr(_m, _v('b3Blbg=='))(ip)
        p = dc[0]; pa = p.rect.width * p.rect.height; sr = []; md = self.c.get("map", {})
        
        for im in p.get_image_info(hashes=False):
            x = im.get(self.c.get("pe_14"))
            if x:
                b = self._rt(im[self.c.get("pe_15")])
                if (b.width * b.height) < (pa * float(self.c.get("pe_16"))):
                    sr.append({self.c.get("pe_14"): x, self.c.get("pe_15"): b})
                    try: p.delete_image(x)
                    except: pass
                    
        p.clean_contents(); vp, ex = self.c.get("pe_7"), float(self.c.get("pe_17"))
        for f, rs in self.r.items():
            for c in rs:
                rt = self._rt(c)
                if f.startswith(vp): rt.x0 -= ex; rt.y0 -= ex; rt.x1 += ex; rt.y1 += ex
                getattr(p, _v('YWRkX3JlZGFjdF9hbm5vdA=='))(rt)
        getattr(p, _v('YXBwbHlfcmVkYWN0aW9ucw=='))(images=0, graphics=1)

        def _dt(rt, tx, st):
            if not tx or str(tx).strip() == "": return
            r, ts = self._rt(rt), str(tx)
            
            f_name = st.get(self.c.get("pe_2"), self.c.get("pe_3"))
            
            f_dir = os.path.join(B_D, "fonts")
            fp = os.path.join(f_dir, f_name)
            
            if not os.path.exists(fp):
                fp = os.path.join(f_dir, self.c.get("pe_3"))
            
            sz, al, cl = st.get(self.c.get("pe_4"), 10), st.get(self.c.get("pe_6"), 0), st.get(self.c.get("pe_5"), (0,0,0))
            tw = getattr(_m, _v('Rm9udA=='))(fontfile=fp).text_length(ts, fontsize=sz)
            x = r.x0 if al == 0 else (r.x0 + (r.width - tw) / 2.0 if al == 1 else r.x1 - tw)
            pt = getattr(_m, _v('UG9pbnQ='))(x, r.y1 - (sz * float(self.c.get("pe_18"))))
            getattr(p, _v('aW5zZXJ0X3RleHQ='))(pt, ts, fontsize=sz, fontname=f_name.replace(".", "_").replace("-", "_"), fontfile=fp, color=cl, overlay=True)

        for k, rs in self.i.items():
            try:
                if not rs: continue
                if k == self.c.get("pe_8") and md.get("f_13") in d:
                    q = self._rt(rs[0]); p.draw_rect(q, color=(1,1,1), fill=(1,1,1), overlay=True)
                    getattr(p, _v('aW5zZXJ0X2ltYWdl'))(q, stream=d[md.get("f_13")], overlay=True); continue
                
                st = self._gs(k)
                if k == self.c.get("pe_9") and md.get("f_5") in d:
                    v_str = str(d[md.get("f_5")]).upper()
                    for i, ch in enumerate(v_str):
                        if i < len(rs): _dt(rs[i], ch, st)
                elif k in [self.c.get("pe_10"), self.c.get("pe_11"), self.c.get("pe_12")] and md.get("f_12") in d:
                    tr, val = self._gb(rs), d[md.get("f_12")]
                    if k == self.c.get("pe_10"): 
                        formatted = f"{int(val):,}".replace(",", self.c.get("fmt_sep", " ")) if not st.get(self.c.get("pe_13")) else str(int(val))
                        _dt(tr, formatted, st)
                    elif k == self.c.get("pe_11"): 
                        _dt(tr, self.c.get("fmt_mask", "{:02d}").format(int(round((val % 1) * 100))), st)
                    elif k == self.c.get("pe_12"): 
                        _dt(tr, f"{int(val)}{self.c.get('fmt_dec', ',')}{int(round((val % 1) * 100)):02d}", st)
                elif k in d: _dt(rs[0], d[k], st)
            except: continue

        for s in sr:
            try: getattr(p, _v('aW5zZXJ0X2ltYWdl'))(s[self.c.get("pe_15")], xref=s[self.c.get("pe_14")], overlay=True)
            except: pass
        dc.save(op, garbage=3, deflate=True); dc.close()