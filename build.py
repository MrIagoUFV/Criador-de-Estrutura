import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'run.py',
    '--onefile',
    '--windowed',
    '--name=CriadorDeEstrutura',
    '--add-data=README.md;.',
    '--icon=icon.ico',
]) 