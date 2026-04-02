# -*- mode: python ; coding: utf-8 -*-
import sysconfig
sp = sysconfig.get_paths()['purelib']

a = Analysis(
    ['music-downloader.py'],
    pathex=[],
    binaries=[],
    datas=[
        (f'{sp}/pykakasi/data', 'pykakasi/data'),
        (f'{sp}/ytmusicapi', 'ytmusicapi'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='music-downloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
