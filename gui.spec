# gui.spec
import sys
import os
from PyInstaller.utils.hooks import collect_all

sys.setrecursionlimit(5000)

# -*- mode: python ; coding: utf-8 -*-

# 1. Список скрытых импортов, которые PyInstaller не видит из-за base64
hiddenimports = ['fitz', 'qrcode']

# 2. Основной конфиг (без него программа не откроется)
datas = [('ui_config.json', '.')]
binaries = []

# 3. Собираем зависимости для customtkinter
tmp_ret = collect_all('customtkinter')
datas += tmp_ret[0]
binaries += tmp_ret[1]
hiddenimports += tmp_ret[2]

a = Analysis(
    ['gui.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    # Исключаем тяжелые библиотеки, если они установлены в системе
    excludes=['matplotlib', 'notebook', 'scipy', 'pandas', 'numpy', 'tkinter.test', 'unittest'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PDF_Template_Engine',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False, # Скрывает консоль при запуске
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PDF_Template_Engine', # Имя папки в dist
)