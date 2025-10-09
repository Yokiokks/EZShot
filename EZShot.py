import time
import keyboard
import datetime
from PIL import ImageGrab
import colorama
from colorama import Fore, Back, Style, init
import pyfiglet
from pyfiglet import Figlet
import os
titulo = pyfiglet.figlet_format("Ez S.hot", font = "alligator")
#// introdução
print(Fore.RED + titulo + Fore.RESET)
print("")
time.sleep(1)
#// Variaveis

numero = 1
#// Tecla

print("Selecione uma tecla")
while(True):
    tecla = input("Insire a Tecla desejada para tirar a captura de tela, caso queira ver a lista de caracteres permitidos coloque 'char': ")
    if tecla == 'char':
        print("""Teclas Especiais: esc, spacebar, capslock, delete, shift,f1,f2,f3,f4,f5,f6,f7,f8,f9,10,f11,f12
        Teclas Normais q,w,e,r,t,y,u,i,o,p,´,[,],a,s,d,f,g,h,j,k,l,ç,~,^,{,}\,|,z,x,c,v,b,n,m, , . ,:,;/.?""")
    else:
        break
    
print("Carregando")
time.sleep(0.5)
os.system("cls")
print("Carregando.")
time.sleep(0.5)
os.system("cls")
print("Carregando..")
time.sleep(0.5)
os.system("cls")
print("Carregando...")
time.sleep(0.5)
os.system("cls")
print("Carregando")
os.system("cls")
time.sleep(0.5)
print("Aplicativo Pronto")
print(f"Pressione {tecla} para Tirar captura de tela")
while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    foto = ImageGrab.grab()
    if keyboard.is_pressed(tecla):
        foto.save(f"{now}.png")
        print(F"foto tirada {now} {numero}")
        numero = numero + 1
        time.sleep(0.5)
        
