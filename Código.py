import win32api
import time
import random
import win32con
import Diccionario


def rev_pal(palabra):

  o=False
  if len(palabra)==int(np): #primero mira que si sea de la longitud que toca

    if palabra in p0:
      o=True #indicador de que si o no hay
  return o


def rev_letras(palabra,respuesta,np,salida):

  for r in range (len(respuesta)):  #Guarda como una variable diferente cada letra de la respuesta
    y=str(r)    
    y="r"+y
    globals()[y]=respuesta[r]

  for pa in range (len(respuesta)): #hace la comparacion letra por letra para el intento
    z=str(pa)
    z="pa"+z
    globals()[z]=palabra[pa] #guarda como una variable la letra de ese momento 

    y=str(pa)
    y="r"+y    #esta notación siempre me toca usarla para poder guardar tantas variables como necesite

    if globals()[z]==globals()[y]:      # compara si son iguales en la misma posicion
      globals()[z]="\033[1;32;40m"+globals()[z]+"\033[1;37;40m"  #lo pone verdecito bonito 
      salida+=1
      
    else:       #compara si son iguales en distinta posición

      for pa in range (len(respuesta)):
        y=str(pa)
        y="r"+y                                                   #la notación

        if globals()[z]==globals()[y]:
          globals()[z]="\033[1;35;40m"+globals()[z]+"\033[1;37;40m"     #  lo pone morado

  intento_color=""
  np=int(np)
  for pa in range (np):   #junta todas las variables (que son letras) para formar la palabra
    z=str(pa)
    z="pa"+z 
    intento_color=intento_color+globals()[z] #concatena y sale pa pintura

  resultados_rev_letras=[intento_color,salida] 
  return resultados_rev_letras          #me figuro hacer lista pq no se como mas retornar varios valores y escoger 1


Vocabsgenie=True #Permite jugar varias veces
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


    intentos=np+1   #fija los intentos con un minimo de 5
    if intentos<5:
      intentos=5
    
    p0=Diccionario.saca_lista(np) #Saca la lista de palabras de np letras
    nrespuesta=random.randint(0,len(p0)-1)#escoje un numero random
    respuesta=p0[nrespuesta] #saca una palabra de ese numero random


    texto="Escriba una palabra de "+str(np)+" letras\n"
    i=1

    while i<=intentos: #funciona por cada intento
      print('\033c')
      print(texto)
      salida=0         #para que salga cuando adivino o lo contrario
      print("\033[1;37;40m") #se asegura de que el default sea letra blanca
      x=str(i)
      x="i"+x           #vida hp
      globals()[x]=str (input())#guarda el intento para luego revisar

      if globals()[x].isalpha():  #Se asegura de que sean solo letras
        globals()[x]=globals()[x].lower()  #quita mayusculas
      else:
        print('\033c')
        continue
  

      if rev_pal(globals()[x]):#si si esta en la lista hace lo de los colorcitos y suma un intento
        i+=1
        texto=texto+rev_letras(globals()[x],respuesta,np,salida)[0]+"\n"

        if rev_letras(globals()[x],respuesta,np,salida)[1]==int(np):
          print('\033c')
          print(texto)
          break

    if rev_letras(globals()[x],respuesta,np,salida)[1]==int(np):#dice si gano o perdio
      print ("\033[1;32;40m Felicidades ganaste en ",i-1," intentos")
      time.sleep(3)
    else:
      print ("\033[1;31;40m Estudie vago")
      time.sleep(1.5)
      print('\033c')
      print("La palabra correcta era: "+respuesta)
      time.sleep(2)

    print('\033c')
    print("Presione el click izquierdo para salir o el derecho para volver a jugar")
    Cde=win32api.GetKeyState(win32con.VK_RBUTTON)
    Ciz=win32api.GetKeyState(win32con.VK_LBUTTON)
    while True:
      if Cde!=win32api.GetKeyState(win32con.VK_RBUTTON):
        time.sleep(0.5)
        break
      if Ciz!=win32api.GetKeyState(win32con.VK_LBUTTON):
        time.sleep(0.5)
        Vocabsgenie=False
        break

print('\033c')
print("\033[1;32;40m Gracias por jugar")
print ("\033[1;31;40m")
time.sleep(2)
print('\033c')  


