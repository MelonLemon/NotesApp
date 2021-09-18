import sys 
import os 
from cx_Freeze import executable, setup, Executable

files = ['logo.ico', "notes.db"]

target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="logo.ico"
)

setup(
    name="Notys",
    version="1.0",
    description="Notes App",
    author="Godlevskaya E.V",
    options={"build_exe" : {"include_files" : files}},
    executables= [target]
)