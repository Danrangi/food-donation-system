# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
    ('app/templates',  'app/templates'),
    ('app/static',     'app/static'),
    ('seed.py',        '.'),
]

a = Analysis(
    ['launcher.py'],
    pathex=['.'],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        'flask',
        'flask_login',
        'flask_sqlalchemy',
        'flask_wtf',
        'flask_bcrypt',
        'werkzeug',
        'werkzeug.security',
        'werkzeug.routing',
        'sqlalchemy',
        'sqlalchemy.dialects.sqlite',
        'sqlalchemy.orm',
        'jinja2',
        'click',
        'itsdangerous',
        'email_validator',
        'app',
        'app.models',
        'app.auth',
        'app.auth.routes',
        'app.donor',
        'app.donor.routes',
        'app.admin',
        'app.admin.routes',
        'app.delivery',
        'app.delivery.routes',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='FoodBridge',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon=None,
)
