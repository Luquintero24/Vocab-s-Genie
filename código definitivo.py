from tkinter import *
from tkinter import messagebox
import Diccionario
import random
from cProfile import label
from tkinter import*
import tkinter as tk
from pygame import *
from PIL import Image,ImageTk,ImageSequence

raiz= Tk()
raiz.title("Vocabs Genie")
raiz.resizable(1,1)
raiz.iconbitmap("icono vocabs genie.ico")
raiz.config(background="black")
img=Image.open("Letras.gif")
img = img.resize((650,650))
newima=ImageTk.PhotoImage(img)
imglabel=Label(raiz,image=newima)
imglabel.image = newima
imglabel.grid(row=0,column=0,columnspan=2,padx=8,pady=8)
imglabel=Label(raiz)

img=Image.open("LOGO VOCAB'S GENIE.png")
img = img.resize((400,400))
newima=ImageTk.PhotoImage(img)
imglabel=Label(raiz,image=newima)
imglabel.image = newima
imglabel.grid(row=0,column=0,columnspan=2,padx=2,pady=2)
imglabel=Label(raiz)
mixer.init()
mixer.music.load("Música.ogg")
mixer.music.play(10)

def abrirventana2():
    raiz.withdraw()
    menu=Tk()
    menu.geometry("650x650")
    menu.config(background="black")
    menu.title("Vocab's Genie Menu")
    Framemenu=Frame(menu,width=650,height=650)
    Framemenu.pack()
    Framemenu.pack(fill="both",expand="True")
    Framemenu.config(background="Black")
    texto1=Label(Framemenu,text="¿Con cuántas letras quieres jugar?",font= "Helvetica 20")
    texto1.config(background= "Pink")
    texto1.place(x=120,y=200)


    def juego():
        menu.withdraw()
        juego=Tk()
        juego.geometry("400x150")
        juego.config(bg="black")
        juego.title("Vocab's Genie")
        Framejuego=Frame(menu,width=80,height=80)
        Framejuego.pack()
        Framejuego.pack(fill="both",expand="True")
        Framejuego.config(background="Black")
        nintentos=0

        Verde= "#059916"
        Amarillo="#f7bf23"
        Negro="#121211"
        Blanco= "#ffffff"
        Gris="#615a59"

        


        Entrada=Entry(juego)
        Entrada.grid(row=999,column=0,padx=50,pady=50,columnspan=3)


        p0=Diccionario.saca_lista(4) #Saca la lista de palabras de np letras
        nrespuesta=random.randint(0,len(p0)-1)#escoje un numero random
        respuesta=p0[nrespuesta] #saca una palabra de ese numero random
        def rev_letras(): 
                
                adivinar= Entrada.get()
                if len(adivinar)==4:
                    adivinar=adivinar.replace("ñ","�")
                    if adivinar in p0:
                        adivinar=adivinar.replace("�","ñ")

                        
                        if respuesta == adivinar:   #Cuando gana
                            messagebox.showinfo("Ganaste!!!"," Felicidades ganaste en ",i-1," intentos")
                        else: #cuando no gana
                            for i, letra in enumerate(adivinar):
                                nintentos=1
                                nintentos+=1
                                label=Label(juego,text=letra.upper())
                                label.grid(row= nintentos,column=i,padx=5,pady=5)

                                if letra==respuesta[i]:  #Letra en correcta posición
                                    label.config(bg=Verde, fg=Negro)
                            
                                if letra in respuesta and not letra == respuesta[i]: #si la letra está pero en diferente posición
                                    label.config(bg=Amarillo, fg= Negro)
                            
                                if letra not in respuesta:
                                    label.config(bg=Negro, fg=Blanco)
                    
                    else:
                        messagebox.showerror("Error", "Esa palabra no está en el diccionario")
                    
                else:
                    messagebox.showerror("Error", "Por favor ingresa una palabra de la cantidad de letras que ingresaste")

        BotonAdivinar= Button(juego, text="Adivinar",command=rev_letras)
        BotonAdivinar.grid(row=999,column=20,columnspan=1)
    nintentos=0      
    Boton2=tk.Button(menu,text="4",width=4,height=4,command=juego).place(x=320,y=320),
    Boton3=tk.Button(menu,text="5",width=4,height=4,command=juego).place(x=270,y=320),
   
        

Boton1=tk.Button(raiz,text="Iniciar",width=10,height=2,command=abrirventana2).place(x=320, y=600)


raiz.mainloop()





