#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

# Definicion del root

root = tk.Tk()

root.title('Abalone')
root.resizable(False, False)

# Definicion del frame

frame = tk.Frame(root, width='1080', height='650')
frame.pack()
frame['bg'] = '#faf9f9'

# Titulo principal

title = tk.Label(frame, text='Abalone Data Analysys', bg='#faf9f9', font=(16))
title.grid(column=0, sticky='E', pady=10)

# Tipo de graficas, definicion del estilo y despliegue de combobox

comboLabel = tk.Label(frame, text='Tipo de gráfica:', bg='#faf9f9',)
comboLabel.grid(row=1, column=0, sticky='W', pady=10)

comboStyle = ttk.Style()
comboStyle.theme_create(
    'combostyle', parent = 'alt',
    settings = {'TCombobox':
                {'configure':
                 {'selectbackground': '#faf9f9',
                  'fieldbackground': '#faf9f9',
                  'background': '#faf9f9'
                  }}}
)

comboStyle.theme_use('combostyle') 

comboGraphs = ttk.Combobox(
    frame,
    state='readonly',
    values=['Histogrma','Diagrama de caja','Disperción','Normalización']    
)
comboGraphs.grid(row=1, column=1, sticky='E', pady=10)

# Variables de entrada, seleccion de las multiples variables de entrada

varLabel = tk.Label(frame, text='Variables de entrada:', bg='#faf9f9')
varLabel.grid(row=2, column=0, sticky='W')

varLenght = tk.IntVar()
varDiameter = tk.IntVar()
varHeight = tk.IntVar()
varWholeWeight = tk.IntVar()
varShuckedWeight = tk.IntVar()
varVisceraWeight = tk.IntVar()
varShellWeight = tk.IntVar()
varRings = tk.IntVar()

chkbtnLenght = tk.Checkbutton(frame, text=' Longitud', bg='#faf9f9', highlightbackground = '#faf9f9', activebackground='#faf9f9', variable=varLenght, onvalue=1, offvalue=0,)
chkbtnLenght.grid(row=2, column=1, sticky='W')

chkbtnDiameter = tk.Checkbutton(frame, text=' Diametro', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varDiameter, onvalue=1, offvalue=0,)
chkbtnDiameter.grid(row=2, column=2, sticky='W')

chkbtnHeight = tk.Checkbutton(frame, text=' Altura', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varHeight, onvalue=1, offvalue=0,)
chkbtnHeight.grid(row=2, column=3, sticky='W')

chkbtnWholeWeight = tk.Checkbutton(frame, text=' Peso completo', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varWholeWeight, onvalue=1, offvalue=0,)
chkbtnWholeWeight.grid(row=3, column=1, sticky='W')

chkbtnShuckedWeight = tk.Checkbutton(frame, text=' Peso de la concha', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varShuckedWeight, onvalue=1, offvalue=0,)
chkbtnShuckedWeight.grid(row=3, column=2, sticky='W')

chkbtnVisceraWeight = tk.Checkbutton(frame, text=' Peso de la víscera', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varVisceraWeight, onvalue=1, offvalue=0,)
chkbtnVisceraWeight.grid(row=3, column=3, sticky='W')

chkbtnShellWeight = tk.Checkbutton(frame, text=' Peso del caparazón', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varShellWeight, onvalue=1, offvalue=0,)
chkbtnShellWeight.grid(row=4, column=1, sticky='W')

chkbtnRings = tk.Checkbutton(frame, text=' Número de anillos', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varRings, onvalue=1, offvalue=0,)
chkbtnRings.grid(row=4, column=2, sticky='W')

# Boton de graficar

btngraph = tk.Button(frame, text='Graficar', activeforeground='#faf9f9' ,activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2')
btngraph.grid(row=5, column=1, sticky='E', pady=10)

# Espera a la accion

root.mainloop()