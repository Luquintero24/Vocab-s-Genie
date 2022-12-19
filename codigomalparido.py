
from tkinter import *
from PySide6.QtGui import QMovie,QIcon
from PySide6.QtWidgets import QLabel, QApplication, QWidget
import sys



class Window(QWidget):
        
    raiz=Tk()
    raiz.title("Vocabs Genie")
    raiz.resizable(1,1)
    raiz.iconbitmap("icono vocabs genie.ico")
raiz.config(background="black")
#raiz.geometry("650x650")
FrameVocabs=Frame()
FrameVocabs.pack()
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100,100,700,500)
        self.setWindowTitle("Vocab's Genie")
        self.setWindowIcon(QIcon('Vocabs Genie.png'))
        
        label =QLabel(self)
        movie = QMovie ('Letras.gif') 
        label.setMovie(movie)
        movie.start()
        
        
app = QApplication([])
window= Window()
window.show()
sys.exit(app.exec())

