import os, re, shutil
import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
root = tk.Tk()
root.geometry("300x150")
root.title("Jogos Loterica")

qtd = ttk.Label(root, text = "Quantidade de Jogos")
qtd.pack(side='top')
value = ttk.Entry()
value.pack(side='top')

num = ttk.Label(root, text = "Quantidade de Numeros")
num.pack(side='top')
value1 = ttk.Entry()
value1.pack(side='top')

rang = ttk.Label(root, text = "range dos jogos 1-")
rang.pack(side='top')
value2 = ttk.Entry()
value2.pack(side='top')


numeros=[]


def gera():
    for i in range (1,int(value2.get())+1):
        numeros.append(i)
    for j in range (1,int(value.get())+1):
        jogo=random.sample(numeros,int(value1.get()))
        file=open("c:/Loteria.txt","a+")
        file.write(str(jogo))
        file.write("\n")
        file.close()

bt = ttk.Button(root,text = 'GO!',command=gera)
bt.pack(side='top')
        
    
