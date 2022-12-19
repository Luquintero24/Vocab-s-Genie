import pygame,sys
from pygame import *
from tkinter import messagebox
from turtle import Screen, width
import pygame,sys
from sys import *
from pygame.locals import *
import pygame.font
from tkinter import  Tk, Button, Entry, Label, messagebox, PhotoImage
from tkinter import  StringVar,Frame

import random
import time


from tkinter import *
from tkinter import ttk

from cProfile import label
import tkinter as tk

from PIL import Image,ImageTk
import customtkinter
from pygame import *
import sys
cancion="Minecraft.ogg"
pygame.init()
SCREEN1=pygame.display.set_mode((1280, 720))
pygame.display.set_caption("VOCABS GENIE")
Icon=pygame.image.load("logo .png")
pygame.display.set_icon(Icon)

Negro=(0,0,0)
Blanco=(255,255,255)

MENU_MOUSE_POS = pygame.mouse.get_pos()
Fuente1=pygame.font.Font("Neonblitz.ttf",90)
Fuente2=pygame.font.Font("Neonblitz.ttf",90)

v_=Rect(100,50,90,90)
o_=Rect(190,50,90,90)
c_=Rect(280,50,90,90)
a_=Rect(370,50,90,90)
b_=Rect(460,50,90,90)
apos_=Rect(540,50,40,90)
s_=Rect(580,50,90,90)
g_=Rect(750,50,90,90)
e_=Rect(840,50,90,90)
n_=Rect(930,50,90,90)
i_=Rect(1020,50,90,90)
ee_=Rect(1110,50,90,90)
v=Fuente2.render("V",True,(3, 252, 235))
o=Fuente2.render("O",True,(235, 52, 52))
c=Fuente2.render("C",True,(3, 252, 235))
a=Fuente2.render("A",True,(235, 52, 52))
b=Fuente2.render("B",True,(3, 252, 235))
apos=Fuente2.render("'",True,(235, 52, 52))
s=Fuente2.render("S",True,(3, 252, 235))
g=Fuente2.render("G",True,(235, 52, 52))
e=Fuente2.render("E",True,(3, 252, 235))
n=Fuente2.render("N",True,(235, 52, 52))
i=Fuente2.render("I",True,(3, 252, 235))
ee=Fuente2.render("E",True,(235, 52, 52))


Inicio=Rect(450,270,450,120)
Mensaje1=Fuente1.render("JUGAR",True,Blanco)
ccancion=Rect(450,570,450,120)
cccancion=Fuente1.render("CANCIÓN",True,Blanco)
Reglas=Rect(450,420,450,120)
Mensaje2=Fuente1.render("REGLAS",True,Blanco)

def cambio_cancion():
    c=random.randint(0,4)
    canciones=["Undertale.ogg","Mario Bros 2.ogg","Minecraft.ogg","Nocturne No.20.ogg","Do i wanna know.ogg" ]
    global cancion
    cancion=canciones[c]
    mixer.stop
    mixer.init()
    mixer.music.load(cancion)
    mixer.music.play(10)

mixer.init()
mixer.music.load(cancion)
mixer.music.play(10)

def screen2():
    



    SCREEN=pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("VOCABS GENIE")
    Icon=pygame.image.load("logo .png")
    pygame.display.set_icon(Icon)
    Negro=(0,0,0)
    Blanco=(255,255,255)
    def menuprincipal():
        pygame.display.set_caption("menu")
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    Fuente3=pygame.font.SysFont("Calibri",30)
    Fuente5=pygame.font.Font("Neonblitz.ttf",170)
    Fuente6=pygame.font.Font("Neonblitz.ttf",60)

    Texto11=Rect(640,300,0,0)
    Texto111=Fuente6.render("Selecciona la cantidad de letras",True, (255,255,0))
    Texto12=Rect(680,380,0,0)
    Texto112=Fuente6.render("con las que quieres jugar",True, (255,255,0))
    menu1=Rect(350,50,150,150)
    mmenu1=Fuente5.render("M",True,(3, 252, 235))
    menu2=Rect(500,50,150,150)
    mmenu2=Fuente5.render("E",True,(235, 52, 52))
    menu3=Rect(650,50,150,150)
    mmenu3=Fuente5.render("N",True,(3, 252, 235))
    menu4=Rect(800,50,150,150)
    mmenu4=Fuente5.render("Ú",True,(235, 52, 52))
    Boton1=Rect(100,500,50,50)
    Mensaje1=Fuente3.render("2",True,Blanco)
    Boton2=Rect(200,500,50,50)
    Mensaje2=Fuente3.render("3",True,Blanco)
    Boton3=Rect(300,500,50,50)
    Mensaje3=Fuente3.render("4",True,Blanco)
    Boton4=Rect(400,500,50,50)
    Mensaje4=Fuente3.render("5",True,Blanco)
    Boton5=Rect(500,500,50,50)
    Mensaje5=Fuente3.render("6",True,Blanco)
    Boton6=Rect(600,500,50,50)
    Mensaje6=Fuente3.render("7",True,Blanco)
    Boton7=Rect(700,500,50,50)
    Mensaje7=Fuente3.render("8",True,Blanco)
    Boton8=Rect(800,500,50,50)
    Mensaje8=Fuente3.render("9",True,Blanco)
    Boton9=Rect(900,500,50,50)
    Mensaje9=Fuente3.render("10",True,Blanco)
    Boton10=Rect(1000,500,50,50)
    Mensaje10=Fuente3.render("11",True,Blanco)
    Boton11=Rect(1100,500,50,50)
    Mensaje11=Fuente3.render("12",True,Blanco)
    Boton12=Rect(1200,500,50,50)
    Mensaje12=Fuente3.render("13",True,Blanco)
    Boton13=Rect(450,600,50,50)
    Mensaje13=Fuente3.render("14",True,Blanco)
    Boton14=Rect(550,600,50,50)
    Mensaje14=Fuente3.render("15",True,Blanco)
    Boton15=Rect(650,600,50,50)
    Mensaje15=Fuente3.render("16",True,Blanco)
    Boton16=Rect(750,600,50,50)
    Mensaje16=Fuente3.render("17",True,Blanco)




    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
            
             sys.exit()
        
        pygame.draw.rect(SCREEN,Blanco,Boton1,0)
        
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            
            if Boton1.collidepoint(pygame.mouse.get_pos()):
                class Wordle2(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:2])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario2.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+" .Solo tenías esta pista :(")
                            a+=2

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==2:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=5:
                                    
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=5,  fg='white' ,
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',53, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =8, pady =5)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=2 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==5 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                    ventana = Tk()
                    ventana.config(bg='black')
                    ventana.iconbitmap('icono vocabs genie.ico')
                    ventana.geometry('1280x720')
                    ventana.resizable(0,0)
                    ventana.title('VOCABS GENIE')
                    app = Wordle2(ventana)
                    app.mainloop()           
                            
            
        if Boton1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton1,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton1,0)
        SCREEN.blit(Mensaje1,(Boton1.x+(Boton1.width-Mensaje1.get_width())/2,Boton1.y+(Boton1.height-Mensaje1.get_height())/2))


        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton2.collidepoint(pygame.mouse.get_pos()):
                class Wordle3(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:3])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario3.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==3:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=5:
                                    
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=5,  fg='white' ,
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',50, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =8, pady =5)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=3 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==5 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                                ventana = Tk()
                                ventana.config(bg='black')
                                ventana.iconbitmap('icono vocabs genie.ico')
                                ventana.geometry('1280x720')
                                ventana.resizable(0,0)
                                ventana.title('VOCABS GENIE')
                                app = Wordle3(ventana)
                                app.mainloop()
                    
            
        if Boton2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton2,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton2,0)
        SCREEN.blit(Mensaje2,(Boton2.x+(Boton2.width-Mensaje2.get_width())/2,Boton2.y+(Boton2.height-Mensaje2.get_height())/2))

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton3.collidepoint(pygame.mouse.get_pos()):
                class Wordle2(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew') 
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:4])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario4.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==4:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=5:
                                    
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=6,  fg='white' ,
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',50, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =8, pady =5)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=4 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==5 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                        ventana = Tk()
                        ventana.config(bg='black')
                        ventana.iconbitmap('icono vocabs genie.ico')
                        ventana.geometry('1280x720')
                        ventana.resizable(0,0)
                        ventana.title('VOCABS GENIE')
                        app = Wordle2(ventana)
                        app.mainloop()           
                
        if Boton3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton3,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton3,0)
        SCREEN.blit(Mensaje3,(Boton3.x+(Boton3.width-Mensaje3.get_width())/2,Boton3.y+(Boton3.height-Mensaje3.get_height())/2))

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton4.collidepoint(pygame.mouse.get_pos()):
                class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:5])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario5.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==5:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=6:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=7,  fg='white' ,
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',40, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =5, pady =5)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=6 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                                ventana = Tk()
                                ventana.config(bg='black')
                                ventana.iconbitmap('icono vocabs genie.ico')
                                ventana.geometry('1280x720')
                                ventana.resizable(0,0)
                                ventana.title('VOCABS GENIE')
                                app = Wordle(ventana)
                                app.mainloop()

        if Boton4.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton4,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton4,0)
        SCREEN.blit(Mensaje4,(Boton4.x+(Boton4.width-Mensaje4.get_width())/2,Boton4.y+(Boton4.height-Mensaje4.get_height())/2))

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton5.collidepoint(pygame.mouse.get_pos()):
                class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:6])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario6.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==6:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=6:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=6,  fg='white' , 
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',36, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =6, pady =5)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=7 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                                ventana = Tk()
                                ventana.config(bg='black')
                                ventana.iconbitmap('icono vocabs genie.ico')
                                ventana.geometry('1280x720')
                                ventana.resizable(0,0)
                                ventana.title('VOCABS GENIE')
                                app = Wordle(ventana)
                                app.mainloop()

        if Boton5.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton5,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton5,0)
        SCREEN.blit(Mensaje5,(Boton5.x+(Boton5.width-Mensaje5.get_width())/2,Boton5.y+(Boton5.height-Mensaje5.get_height())/2))

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton6.collidepoint(pygame.mouse.get_pos()):
                class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:7])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario7.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==7:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=7:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=5,  fg='white' , 
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',38, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =7, pady =3)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=7 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                                ventana = Tk()
                                ventana.config(bg='black')
                                ventana.iconbitmap('icono vocabs genie.ico')
                                ventana.geometry('1280x720')
                                ventana.resizable(0,0)
                                ventana.title('VOCABS GENIE')
                                app = Wordle(ventana)
                                app.mainloop()

            
        if Boton6.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton6,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton6,0)
        SCREEN.blit(Mensaje6,(Boton6.x+(Boton6.width-Mensaje6.get_width())/2,Boton6.y+(Boton6.height-Mensaje6.get_height())/2))

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton7.collidepoint(pygame.mouse.get_pos()):
                class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:8])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario8.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==8:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=8:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=6,  fg='white' , 
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',30, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =4, pady =2)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=7 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                                ventana = Tk()
                                ventana.config(bg='black')
                                ventana.iconbitmap('icono vocabs genie.ico')
                                ventana.geometry('1280x720')
                                ventana.resizable(0,0)
                                ventana.title('VOCABS GENIE')
                                app = Wordle(ventana)
                                app.mainloop()

        if Boton7.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton7,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton7,0)
        SCREEN.blit(Mensaje7,(Boton7.x+(Boton7.width-Mensaje7.get_width())/2,Boton7.y+(Boton7.height-Mensaje7.get_height())/2))

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton8.collidepoint(pygame.mouse.get_pos()):
                class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:9])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario9.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==9:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=9:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=6,  fg='white' , 
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',24, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =4, pady =3)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=7 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                                ventana = Tk()
                                ventana.config(bg='black')
                                ventana.iconbitmap('icono vocabs genie.ico')
                                ventana.geometry('1280x720')
                                ventana.resizable(0,0)
                                ventana.title('VOCABS GENIE')
                                app = Wordle(ventana)
                                app.mainloop()

        if Boton8.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton8,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton8,0)
        SCREEN.blit(Mensaje8,(Boton8.x+(Boton8.width-Mensaje8.get_width())/2,Boton8.y+(Boton8.height-Mensaje8.get_height())/2))
        

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton9.collidepoint(pygame.mouse.get_pos()):
                class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:10])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario10.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==10:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=10:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=6,  fg='white' , 
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',23, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =2, pady =2)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=7 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                                ventana = Tk()
                                ventana.config(bg='black')
                                ventana.iconbitmap('icono vocabs genie.ico')
                                ventana.geometry('1280x720')
                                ventana.resizable(0,0)
                                ventana.title('VOCABS GENIE')
                                app = Wordle(ventana)
                                app.mainloop()

            
        if Boton9.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton9,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton9,0)
        SCREEN.blit(Mensaje9,(Boton9.x+(Boton9.width-Mensaje9.get_width())/2,Boton9.y+(Boton9.height-Mensaje9.get_height())/2))


        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton10.collidepoint(pygame.mouse.get_pos()):
                class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:11])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario11.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==11:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=11:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=6,  fg='white' , 
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',20, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =2, pady =1)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=7 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                                ventana = Tk()
                                ventana.config(bg='black')
                                ventana.iconbitmap('icono vocabs genie.ico')
                                ventana.geometry('1280x720')
                                ventana.resizable(0,0)
                                ventana.title('VOCABS GENIE')
                                app = Wordle(ventana)
                                app.mainloop()

            
        if Boton10.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton10,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton10,0)
        SCREEN.blit(Mensaje10,(Boton10.x+(Boton10.width-Mensaje10.get_width())/2,Boton10.y+(Boton10.height-Mensaje10.get_height())/2))

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton11.collidepoint(pygame.mouse.get_pos()):
                class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:12])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario12.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==12:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=12:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=6,  fg='white' , 
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',18, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =2, pady =1)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=7 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                                ventana = Tk()
                                ventana.config(bg='black')
                                ventana.iconbitmap('icono vocabs genie.ico')
                                ventana.geometry('1280x720')
                                ventana.resizable(0,0)
                                ventana.title('VOCABS GENIE')
                                app = Wordle(ventana)
                                app.mainloop()

        if Boton11.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton11,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton11,0)
        SCREEN.blit(Mensaje11,(Boton11.x+(Boton11.width-Mensaje11.get_width())/2,Boton11.y+(Boton11.height-Mensaje11.get_height())/2))
        

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton12.collidepoint(pygame.mouse.get_pos()):
                class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:13])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario13.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==13:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=13:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=6,  fg='white' , 
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',17, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =1, pady =1)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=7 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                            ventana = Tk()
                            ventana.config(bg='black')
                            ventana.iconbitmap('icono vocabs genie.ico')
                            ventana.geometry('1280x720')
                            ventana.resizable(0,0)
                            ventana.title('VOCABS GENIE')
                            app = Wordle(ventana)
                            app.mainloop()

            
        if Boton12.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton12,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton12,0)
        SCREEN.blit(Mensaje12,(Boton12.x+(Boton12.width-Mensaje12.get_width())/2,Boton12.y+(Boton12.height-Mensaje12.get_height())/2))
        

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton13.collidepoint(pygame.mouse.get_pos()):
                class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:14])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario14.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==14:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=14:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=6,  fg='white' , 
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',16, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =1, pady =1)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=7 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                            ventana = Tk()
                            ventana.config(bg='black')
                            ventana.iconbitmap('icono vocabs genie.ico')
                            ventana.geometry('1280x720')
                            ventana.resizable(0,0)
                            ventana.title('VOCABS GENIE')
                            app = Wordle(ventana)
                            app.mainloop()

            
        if Boton13.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton13,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton13,0)
        SCREEN.blit(Mensaje13,(Boton13.x+(Boton13.width-Mensaje13.get_width())/2,Boton13.y+(Boton13.height-Mensaje13.get_height())/2))
        

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton14.collidepoint(pygame.mouse.get_pos()):
                class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:15])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario15.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==15:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=15:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=6,  fg='white' , 
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',14, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =1, pady =1)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=7 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                            ventana = Tk()
                            ventana.config(bg='black')
                            ventana.iconbitmap('icono vocabs genie.ico')
                            ventana.geometry('1280x720')
                            ventana.resizable(0,0)
                            ventana.title('VOCABS GENIE')
                            app = Wordle(ventana)
                            app.mainloop()

        if Boton14.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton14,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton14,0)
        SCREEN.blit(Mensaje14,(Boton14.x+(Boton14.width-Mensaje14.get_width())/2,Boton14.y+(Boton14.height-Mensaje14.get_height())/2))
        

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton15.collidepoint(pygame.mouse.get_pos()):
                class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:16])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario16.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==16:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=16:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=7,  fg='white' , 
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',13, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =1, pady =1)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=7 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                if __name__ == "__main__":
                            ventana = Tk()
                            ventana.config(bg='black')
                            ventana.iconbitmap('icono vocabs genie.ico')
                            ventana.geometry('1280x720')
                            ventana.resizable(0,0)
                            ventana.title('VOCABS GENIE')
                            app = Wordle(ventana)
                            app.mainloop()

        if Boton15.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton15,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton15,0)
        SCREEN.blit(Mensaje15,(Boton15.x+(Boton15.width-Mensaje15.get_width())/2,Boton15.y+(Boton15.height-Mensaje15.get_height())/2))
        

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Boton16.collidepoint(pygame.mouse.get_pos()):
                    class Wordle(Frame):
                        def __init__(self, master):
                            super().__init__( master)
                            self.fila = 0
                            self.verde = '#03fceb'
                            self.naranjado = '#eb3434'
                            self.gris = '#8F8E8C'
                            self.morado= '#fc03fc'
                            self.texto = StringVar()
                            self.texto.trace("w", lambda *args: self.limitar(self.texto))
                            self.create_widgets()
                            self.palabra_aleatoria()

                        def create_widgets(self):
                            self.frame_titulo = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_titulo.grid_propagate(0)
                            self.frame_titulo.grid(column=1, row=0, sticky='snew')
                            self.frame_cuadros = Frame(self.master, bg='black', width=1240, height=500)
                            self.frame_cuadros.grid_propagate(0)
                            self.frame_cuadros.grid(column=1, row=1, sticky='snew')
                            self.frame_control = Frame(self.master, bg='black', width=1240, height=100)
                            self.frame_control.grid_propagate(0)
                            self.frame_control.grid(column=1, row=2, sticky='snew')

                            Label(self.frame_titulo,  bg= 'black',fg='white', text= 'VOCABS GENIE', 
                                font=('Arial',50,'bold')).pack(side='top')

                            self.signal = Label(self.frame_control,  bg= 'black',fg='white', text= 'Señal', 
                                font=('Arial',30))
                            self.signal.pack(side= 'left', expand=True)

                            self.palabra = Entry(self.frame_control, font=('Arial',35), justify = 'center', 
                                textvariable = self.texto,fg='black',highlightcolor= "green2", highlightthickness=2, width=7)
                            self.palabra.pack(side= 'left', expand=True)

                            self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), command=self.verificar_palabra)
                            self.enviar.pack(side= 'left', expand=True)

                            self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command= lambda:self.texto.set(''))
                            self.limpiar.pack(side= 'left', expand=True)

                            self.pista = Button(self.frame_control, text= 'Pista', bg='gray50',activebackground='green2',
                            fg = 'white', font=('Arial', 25,'bold'), width=6, command=self.pista)
                            self.pista.pack(side= 'left', expand=True)

                        def limitar(self, texto):
                            if len(texto.get()) > 0:
                                texto.set(texto.get()[:17])

                        def palabra_aleatoria(self):
                            archivo = open('Diccionario17.txt','r',encoding="utf-8") #leer la Ñ
                            self.lista = archivo.readlines()
                            self.p_a =  random.choice(self.lista).rstrip('\n') 
                            global a
                            a=0
                        
                        def pista(self):
                            x=random.randint(0,len(self.p_a)-1)
                            ppista=""
                            global a
                            for i in range(len(self.p_a)):
                                if i==x:
                                    ppista+=self.p_a[i]
                                else:
                                    ppista+="�"
                            pistas_n=len(self.p_a)//2-a
                            if a<=(len(self.p_a)//2):
                                messagebox.showinfo("PISTA",ppista.upper()+"  Te quedan "+str(pistas_n)+" pistas")
                            a+=1

                        def verificar_palabra(self):
                            palabra = self.texto.get().lower()
                            palabra=palabra.replace("ñ","�")
                            palabra=palabra.replace("á","a")
                            palabra=palabra.replace("é","e")
                            palabra=palabra.replace("í","i")
                            palabra=palabra.replace("ó","o")
                            palabra=palabra.replace("ú","u")
                            x = list(filter(lambda x: palabra in x, self.lista)) #[i for i in lista if palabra in i]
                            if len(x)==1 and len(palabra)==17:
                                self.signal['text'] = ''
                                print(self.p_a, palabra)			
                                if self.fila<=17:					
                                    for i, letra in enumerate(palabra):
                                        letra=letra.replace("�","ñ")
                                        
                                        self.cuadros = Label(self.frame_cuadros, width=7,  fg='white' , 
                                            bg=self.gris, text= letra.upper(), font=('Geometr706 BlkCn BT',11, 'bold'))
                                        self.cuadros.grid(column=i, row = self.fila , padx =1, pady =1)
                                        if letra == self.p_a[i]:
                                            self.cuadros['bg']= self.verde

                                        if letra in self.p_a and not letra== self.p_a[i]:
                                            self.cuadros['bg']= self.naranjado

                                        if letra not in self.p_a:
                                            self.cuadros['bg']= self.gris

                                self.fila = self.fila + 1
                                if self.fila<=7 and self.p_a == palabra:
                                    messagebox.showinfo("¡GANASTE!","¡FELICIDADES!, GANASTE EN "+str(self.fila)+" INTENTOS")
                                    self.master.destroy()
                                    self.master.quit()				
                                if self.fila==len(self.p_a)+1 and self.p_a != palabra:
                                    messagebox.showinfo("¡PERDISTE!"," La palabra correcta es: "+str(self.p_a).upper()+" . Inténtalo de nuevo")
                                    self.master.destroy()
                                    self.master.quit()
                            else:
                                self.signal['text'] = 'No esta en el diccionario'

                    if __name__ == "__main__":
                                    ventana = Tk()
                                    ventana.config(bg='black')
                                    ventana.iconbitmap('icono vocabs genie.ico')
                                    ventana.geometry('1280x720')
                                    ventana.resizable(0,0)
                                    ventana.title('VOCABS GENIE')
                                    app = Wordle(ventana)
                                    app.mainloop()
            
            
        if Boton16.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN,(237,128,19),Boton16,0)
        else:
            pygame.draw.rect(SCREEN,Negro,Boton16,0)
        SCREEN.blit(Mensaje16,(Boton16.x+(Boton16.width-Mensaje16.get_width())/2,Boton16.y+(Boton16.height-Mensaje16.get_height())/2))

        pygame.draw.rect(SCREEN,Negro,menu1,0)
        SCREEN.blit(mmenu1,(menu1.x+(menu1.width-mmenu1.get_width())/2,menu1.y+(menu1.height-mmenu1.get_height())/2))
        pygame.draw.rect(SCREEN,Negro,menu2,0)
        SCREEN.blit(mmenu2,(menu2.x+(menu2.width-mmenu2.get_width())/2,menu2.y+(menu2.height-mmenu2.get_height())/2))
        pygame.draw.rect(SCREEN,Negro,menu3,0)
        SCREEN.blit(mmenu3,(menu3.x+(menu3.width-mmenu3.get_width())/2,menu3.y+(menu3.height-mmenu3.get_height())/2))
        pygame.draw.rect(SCREEN,Negro,menu4,0)
        SCREEN.blit(mmenu4,(menu4.x+(menu4.width-mmenu4.get_width())/2,menu4.y+(menu4.height-mmenu4.get_height())/2))
        pygame.draw.rect(SCREEN,Negro,Texto11,0)
        SCREEN.blit(Texto111,(Texto11.x+(Texto11.width-Texto111.get_width())/2,Texto11.y+(Texto11.height-Texto111.get_height())/2))
        pygame.draw.rect(SCREEN,Negro,Texto12,0)
        SCREEN.blit(Texto112,(Texto12.x+(Texto12.width-Texto112.get_width())/2,Texto12.y+(Texto12.height-Texto112.get_height())/2))

        pygame.display.update()
 
def reglas():   
    messagebox.showinfo("REGLAS","1. Tienes que adivinar una palabra usando otras palabras \n2. Tienes intentos limitados al numero de letras que escogiste mas 1 \n3. Letras AZULES estan en la posicion correcta\n4. Letras ROJAS NO estan en la posicion correcta\n5. Letras grises no estan\n6. Tienes pistas limitadas a la mitad entera del numero de letras\n7. Si pierdes siempre puedes volver a jugar\n8. Diviertete, te queremos :) <3 ")

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
            
                sys.exit()
        
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            
            if Inicio.collidepoint(pygame.mouse.get_pos()):
                screen2()
        if Inicio.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),Inicio,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,Inicio,0)
        SCREEN1.blit(Mensaje1,(Inicio.x+(Inicio.width-Mensaje1.get_width())/2,Inicio.y+(Inicio.height-Mensaje1.get_height())/2))

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if Reglas.collidepoint(pygame.mouse.get_pos()):
                reglas()
        if Reglas.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),Reglas,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,Reglas,0)
        SCREEN1.blit(Mensaje2,(Reglas.x+(Reglas.width-Mensaje2.get_width())/2,Reglas.y+(Reglas.height-Mensaje2.get_height())/2))

        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if ccancion.collidepoint(pygame.mouse.get_pos()):
                cambio_cancion()
        if ccancion.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),ccancion,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,ccancion,0)
        SCREEN1.blit(cccancion,(ccancion.x+(ccancion.width-cccancion.get_width())/2,ccancion.y+(ccancion.height-cccancion.get_height())/2))


        if v_.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),v_,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,v_,0)
        SCREEN1.blit(v,(v_.x+(v_.width-v.get_width())/2,v_.y+(v_.height-v.get_height())/2))

        if o_.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),o_,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,o_,0)
        SCREEN1.blit(o,(o_.x+(o_.width-o.get_width())/2,o_.y+(o_.height-o.get_height())/2))

        if c_.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),c_,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,c_,0)
        SCREEN1.blit(c,(c_.x+(c_.width-c.get_width())/2,c_.y+(c_.height-c.get_height())/2))

        if a_.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),a_,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,a_,0)
        SCREEN1.blit(a,(a_.x+(a_.width-a.get_width())/2,a_.y+(a_.height-a.get_height())/2))

        if b_.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),b_,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,b_,0)
        SCREEN1.blit(b,(b_.x+(b_.width-b.get_width())/2,b_.y+(b_.height-b.get_height())/2))

        if apos_.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),apos_,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,apos_,0)
        SCREEN1.blit(apos,(apos_.x+(apos_.width-apos.get_width())/2,apos_.y+(apos_.height-apos.get_height())/2))

        if s_.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),s_,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,s_,0)
        SCREEN1.blit(s,(s_.x+(s_.width-s.get_width())/2,s_.y+(s_.height-s.get_height())/2))

        if g_.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),g_,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,g_,0)
        SCREEN1.blit(g,(g_.x+(g_.width-g.get_width())/2,g_.y+(g_.height-g.get_height())/2))

        if e_.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),e_,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,e_,0)
        SCREEN1.blit(e,(e_.x+(e_.width-e.get_width())/2,e_.y+(e_.height-e.get_height())/2))

        if n_.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),n_,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,n_,0)
        SCREEN1.blit(n,(n_.x+(n_.width-n.get_width())/2,n_.y+(n_.height-n.get_height())/2))

        if i_.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),i_,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,i_,0)
        SCREEN1.blit(i,(i_.x+(i_.width-i.get_width())/2,i_.y+(i_.height-i.get_height())/2))

        if ee_.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(SCREEN1,(237,128,19),ee_,0)
        else:
            pygame.draw.rect(SCREEN1,Negro,ee_,0)
        SCREEN1.blit(ee,(ee_.x+(ee_.width-ee.get_width())/2,ee_.y+(ee_.height-ee.get_height())/2))

        pygame.display.update()

main_menu()