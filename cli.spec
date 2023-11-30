# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['liquidctl\\cli.py'],
    pathex=['venv\\Lib\\site-packages\\'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['venv\\Lib\\site-packages\\Pyinstaller','venv\\Lib\\site-packages\\pyinstaller-6.2.0.dist-info\\'],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='liquidCtl',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='AMD64',
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='liquidCtl',
)
