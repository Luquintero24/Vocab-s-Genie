from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
ventana=Tk()
ventana.title("Vocab's Genie")
ventana.iconbitmap("icono vocabs genie.ico")
ventana.resizable(False,False)



img=Image.open("Letras.gif")
img = img.resize((650,650), Image.ANTIALIAS)
newima=ImageTk.PhotoImage(img)
imglabel=Label(ventana,image=newima)
imglabel.image = newima
imglabel.grid(row=0,column=0,columnspan=2,padx=8,pady=8)
imglabel=Label(ventana)

img=Image.open("LOGO VOCAB'S GENIE.png")
img = img.resize((400,400), Image.ANTIALIAS)
newima=ImageTk.PhotoImage(img)
imglabel=Label(ventana,image=newima)
imglabel.image = newima
imglabel.grid(row=0,column=0,columnspan=2,padx=2,pady=2)
imglabel=Label(ventana)
def canletras():
    Vocabsgenie=True
    while Vocabsgenie:
    
        z=True
        while z:#se asegura de que escojan un numero aceptable con una interfaz bonita
            print('\033c')
        np=str (input("\033c Escoja el numero de letras con el que quiere jugar:   "))

        if np.isdigit():
            np=int(np)
        else:
            continue

        if np<=1:
            print("Escoja un numero mayor a 1")
            time.sleep(1)
            continue

        elif np>17:
            print("Escoja un numero menor a 5")
            time.sleep(1)
            continue

        z=False;            #se asegura de que el numero sea mayor a 2 y deja reelegir cuando no
        print('\033c')


Button(ventana,text="Iniciar",command=canletras).place(x= 450, y=300)
ventana.mainloop()

