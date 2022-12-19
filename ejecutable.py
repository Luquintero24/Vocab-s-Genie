from ensurepip import version
from http.server import executable
import sys
import os 

from cx_Freeze import setup, Executable

files= ['Música','Diccionarios']
Executable(script='VOCABS GENIE.py', base='Win32GUI')

setup(
    name="VOCABS GENIE"
    version="1.0"
    description="Un juego de palabras para incrementar tu vocabulario"
    options={"build_exe" : ("Include_files": files)},
    executables= [exe]
    


)