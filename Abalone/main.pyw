#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importacion de bibliotecas y paquetes necesarios para la ejecucion del aplicativo

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk
from scipy import stats
import tkinter as tk
import numpy as np
import dataset as ds

# Definicion de la clase de la aplicacion

class main():
    
    # Importacion del dataset del abalone mediante la creacion de un objeto de la clase DataSet

    dataSetObject = ds.dataSet('abalone.csv')
    dataSetObject.setColums(["Sex", "Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "Rings"])

    # Definicion del root y del frame

    root = tk.Tk()
    frame = tk.Frame(root)

    # Titulo principal

    title = tk.Label(frame, text='Abalone Data Analysys', bg='#faf9f9', font=('Segoe UI', 18, 'bold'))

    # Despliegue del tipo de graficas

    comboLabel = tk.Label(frame, text='Tipo de gráfica:', bg='#faf9f9', font=('Segoe UI', 10))
    comboStyle = ttk.Style()
    comboGraphs = ttk.Combobox(
    frame,
    state='readonly',
    font=('Segoe UI', 10),
    values=['Histograma','Diagrama de caja','Dispersión','Normalización']
    )

    # Definicion de las variables de entrada y los campos de seleccion

    varLabel = tk.Label(frame, text='Variables de entrada:', bg='#faf9f9', font=('Segoe UI', 10))

    varInputLenght = tk.IntVar()
    varInputDiameter = tk.IntVar()
    varInputHeight = tk.IntVar()
    varInputWholeWeight = tk.IntVar()
    varInputShuckedWeight = tk.IntVar()
    varInputVisceraWeight = tk.IntVar()
    varInputShellWeight = tk.IntVar()
    varInputRings = tk.IntVar()

    chkbtnInputLenght = tk.Checkbutton(frame, text=' Longitud', bg='#faf9f9', highlightbackground = '#faf9f9', activebackground='#faf9f9', variable=varInputLenght, onvalue=1, offvalue=0)
    chkbtnInputDiameter = tk.Checkbutton(frame, text=' Diametro', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputDiameter, onvalue=1, offvalue=0)
    chkbtnInputHeight = tk.Checkbutton(frame, text=' Altura', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputHeight, onvalue=1, offvalue=0)
    chkbtnInputWholeWeight = tk.Checkbutton(frame, text=' Peso completo', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputWholeWeight, onvalue=1, offvalue=0)    
    chkbtnInputShuckedWeight = tk.Checkbutton(frame, text=' Peso de la concha', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputShuckedWeight, onvalue=1, offvalue=0)
    chkbtnInputVisceraWeight = tk.Checkbutton(frame, text=' Peso de la víscera', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputVisceraWeight, onvalue=1, offvalue=0)
    chkbtnInputShellWeight = tk.Checkbutton(frame, text=' Peso del caparazón', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputShellWeight, onvalue=1, offvalue=0)
    chkbtnInputRings = tk.Checkbutton(frame, text=' Número de anillos', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRings, onvalue=1, offvalue=0)

    # Datos atipicos

    atypicalLabel = tk.Label(frame, text='Valor del factor de alpha para los atípicos:', bg='#faf9f9', font=('Segoe UI', 10))
    atypicalInput = ttk.Entry(frame)
    btnAtypical = tk.Button(frame, text='Eliminar atípicos', activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2', font=('Segoe UI', 10))

    # Definicion del boton de realizar el resumen estadistico
    
    btnsummary = tk.Button(frame, text='Resumen estadístico', activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2', font=('Segoe UI', 10))

    # Definicion del boton de graficar

    btngraph = tk.Button(frame, text='Graficar', activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2', font=('Segoe UI', 10))

    def __init__(self):
        super().__init__()

        # Modificacion de propiedades del root

        self.root.title('Abalone')
        self.root.resizable(False, False)   

        # Modificacion de propiedades del frame

        self.frame.pack()
        self.frame['bg'] = '#faf9f9'

        # Titulo principal - Ubicacion en el grid

        self.title.grid(column=1, columnspan=2, sticky='NWES', pady=10)

        # Tipo de graficas, definicion del estilo, despliegue de combobox y ubicacion en el grid

        self.comboLabel.grid(row=1, column=0, sticky='W', pady=10)

        self.comboStyle.theme_create(
            'combostyle', parent = 'alt',
            settings = {'TCombobox':
                        {'configure':
                        {'selectbackground': '#555B6E',
                        'fieldbackground': '#555B6E',
                        'background': '#555B6E',
                        }}}
        )

        self.comboStyle.theme_use('combostyle') 

        self.comboGraphs.config(foreground='#faf9f9')
        self.comboGraphs.current(0)
        self.comboGraphs.grid(row=1, column=1, sticky='E', pady=15)

        # Variables de entrada y seleccion de los campos para las mismas - Ubicacion en el grid

        self.varLabel.grid(row=2, column=0, sticky='W')

        self.chkbtnInputLenght.grid(row=2, column=1, sticky='W')
        self.chkbtnInputDiameter.grid(row=2, column=2, sticky='W')
        self.chkbtnInputHeight.grid(row=2, column=3, sticky='W')
        self.chkbtnInputWholeWeight.grid(row=3, column=1, sticky='W')
        self.chkbtnInputShuckedWeight.grid(row=3, column=2, sticky='W')
        self.chkbtnInputVisceraWeight.grid(row=3, column=3, sticky='W')
        self.chkbtnInputShellWeight.grid(row=4, column=1, sticky='W')
        self.chkbtnInputRings.grid(row=4, column=2, sticky='W')

        # Datos atipicos, ubicacion en el grid y definicion del comando de ejecucion para el boton

        self.atypicalLabel.grid(row=5, column=0, columnspan=2, sticky='NW', pady=15)

        self.atypicalInput.grid(row=5, column=2, sticky='W', padx=10)

        self.btnAtypical.grid(row=5, column=3, pady=15)
        self.btnAtypical.config(command=self.removeAtypics)

        # Definicion del comando a ejecutar para el boton de realizar la regresion y ubicacion en el grid

        self.btnsummary.grid(row=6, column=1, sticky='WE', padx=5, pady=10)
        self.btnsummary.config(command=self.summary)

        # Definicion del comando a ejecutar para el boton de graficar y bicacion en el grid

        self.btngraph.grid(row=6, column=2, sticky='WE', padx=5, pady=10)
        self.btngraph.config(command=self.graph)

    # Metodo de generacion de ventana emergente para mostrar alertas u errores

    def newWindow(self, title, message):

        # Creacion de la nueva ventana

        newgraphWindow = tk.Toplevel(self.root)
        newgraphWindow.resizable(False, False)
        newgraphWindow.title(title)
        
        # Creacion de la figura a graficar

        frame = tk.Frame(newgraphWindow, width='1080', height='650')
        frame.pack()
        frame['bg'] = '#faf9f9' 
        
        # Creacion del encabezado y el boton de cerrar de la ventana

        lbl = tk.Label(frame, text=message, bg='#faf9f9', font=(16))
        lbl.grid(row=0)
    
        btnClose = tk.Button(frame, text="Cerrar", activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2', command=lambda: newgraphWindow.destroy(), font=('Segoe UI', 10))
        btnClose.grid(row=1, pady=10)
    
    # Metodo de identificacion de las variables seleccionadas

    def checkSelectedInput(self):
        selectedInput = []
        
        if self.varInputLenght.get() == 1:
            selectedInput.append('Length')
        if self.varInputDiameter.get() == 1:
            selectedInput.append('Diameter')
        if self.varInputHeight.get() == 1:
            selectedInput.append('Height')
        if self.varInputWholeWeight.get() == 1:
            selectedInput.append('Whole weight')
        if self.varInputShuckedWeight.get() == 1:
            selectedInput.append('Shucked weight')
        if self.varInputVisceraWeight.get() == 1:
            selectedInput.append('Viscera weight')
        if self.varInputShellWeight.get() == 1:
            selectedInput.append('Shell weight')
        if self.varInputRings.get() == 1:
            selectedInput.append('Rings')
        
        return selectedInput

    # Metodo de graficacion de los datos

    def graph(self):
        
        # Creacion de la nueva ventana de graficacion

        newgraphWindow = tk.Toplevel(self.root)
        newgraphWindow.resizable(False, False)
        
        frame = tk.Frame(newgraphWindow)
        frame.pack()
        frame['bg'] = '#faf9f9'
        
        # Creacion de la figura a graficar

        f = Figure(figsize=(5,4), dpi=100)
        canvas = FigureCanvasTkAgg(f, master=frame)
        plot = f.gca()

        # Obtencion de los campos de entrada a traves de la interfaz

        selectedInput = self.checkSelectedInput()
        incoherence = False
        graphType = self.comboGraphs.get()
        subtitle = ''

        # Realizacion de la grafica segun el tipo

        subtitle = str(selectedInput[0])

        if (len(selectedInput) == 1):


            if (graphType == 'Histograma'):
                plot.hist(self.dataSetObject.data[selectedInput[0]])

            elif (graphType == 'Diagrama de caja'):
                plot.boxplot(self.dataSetObject.data[selectedInput[0]])

            elif (graphType == 'Normalización'):
                graph = plot.figure()
                ax = graph.add_subplot(111)
                stats.probplot(self.dataSetObject.data[selectedInput[0]], dist=stats.norm, sparams=(6,), plot=ax)
            
            else:
                incoherence = True

        elif (len(selectedInput) == 2):

            if (graphType == 'Dispersión'):
                plot.scatter(self.dataSetObject.data[selectedInput[0]], self.dataSetObject.data[selectedInput[1]])
                subtitle += ' - ' + str(selectedInput[1])

            else:
                incoherence = True

        else:

            incoherence = True

        if incoherence == True:
            self.newWindow('Error','Recuerda, para realizar un histograma, un diagrama de caja o un gráfico de normalización se requiere \n únicamente que tengas una variable de entrada seleccionada, pero, para realizar un gráfico de dispersión \n se requiere que tengas dos variables de entrada seleccionadas.')
            return

        # Creacion del encabezado, subtitulo y el boton de cerrar de la ventana

        lbl = tk.Label(frame, text=graphType, bg='#faf9f9', font=('Segoe UI', 18, 'bold'))
        lbl.grid(row=0, column=1, columnspan=2, sticky='WE', pady=5)

        lbl = tk.Label(frame, text=subtitle, bg='#faf9f9', font=('Segoe UI', 12))
        lbl.grid(row=1, column=1, columnspan=2, sticky='WE', pady=1)
    
        btnClose = tk.Button(frame, text="Cerrar", activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2', command=lambda: newgraphWindow.destroy(), font=('Segoe UI', 10))
        btnClose.grid(row=5, column=2 ,pady=10, sticky='W')

        # Muestra de la grafica en la ventana

        canvas.get_tk_widget().grid(row=2, column=1, rowspan=3, columnspan=2)

    # Metodo para eliminar y restaurar los datos atipicos
    
    def removeAtypics(self):
        
        # Eliminacion de datos atipicos

        if (self.btnAtypical['text'] == 'Eliminar atípicos'):

            alpha = self.atypicalInput.get()

            maxlimits = []
            minlimits = []
            
            try:
                for i in range (1, len(self.dataSetObject.data.columns)):
                    q75 = np.quantile(self.dataSetObject.data[self.dataSetObject.data.columns[i]],.75)
                    q25 = np.quantile(self.dataSetObject.data[self.dataSetObject.data.columns[i]],.25)
                    intr_qr = q75 - q25

                    maxlimits.append(q75 + (float(alpha) * intr_qr))
                    minlimits.append(q25 - (float(alpha) * intr_qr))

                self.dataSetObject.data = self.dataSetObject.copyData[(self.dataSetObject.copyData['Length'] < maxlimits[0]) & (self.dataSetObject.copyData['Length'] > minlimits[0]) & (self.dataSetObject.copyData['Diameter'] < maxlimits[1]) & (self.dataSetObject.copyData['Diameter'] > minlimits[1]) & (self.dataSetObject.copyData['Height'] < maxlimits[2]) & (self.dataSetObject.copyData['Height'] > minlimits[2]) & (self.dataSetObject.copyData['Whole weight'] < maxlimits[3]) & (self.dataSetObject.copyData['Whole weight'] > minlimits[3]) & (self.dataSetObject.copyData['Shucked weight'] < maxlimits[4]) & (self.dataSetObject.copyData['Shucked weight'] > minlimits[4]) & (self.dataSetObject.copyData['Viscera weight'] < maxlimits[5]) & (self.dataSetObject.copyData['Viscera weight'] > minlimits[5]) & (self.dataSetObject.copyData['Shell weight'] < maxlimits[6]) & (self.dataSetObject.copyData['Shell weight'] > minlimits[6]) & (self.dataSetObject.copyData['Rings'] < maxlimits[7]) & (self.dataSetObject.copyData['Rings'] > minlimits[7])]
                self.newWindow('Solicitud exitosa', 'La remosión de los datos atípicos se ha realizado de manera exitosa')
                self.btnAtypical['text'] = 'Restaurar atípicos'

            except:
                self.newWindow('Error','Ups, algo ha salido mal, revisa que el valor de alpha sea valido')
                return

        # Restauracion de los datoos atipicos

        else:

            self.dataSetObject.data = self.dataSetObject.copyData.copy()
            self.newWindow('Solicitud exitosa', 'La restauración de los datos atípicos se ha realizado de manera exitosa')
            self.btnAtypical['text'] = 'Eliminar atípicos'
        

        self.atypicalInput.delete(0,tk.END)


    def summary(self):
        
        newgraphWindow = tk.Toplevel(self.root)
        newgraphWindow.resizable(False, False)
        
        frame = tk.Frame(newgraphWindow)
        frame.pack()
        frame['bg'] = '#faf9f9'

        #generalInfo = []
        #info = []

        # Label de encabezados superiores de la tabla

        content = tk.Label(frame, text='Media', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=1, column=2, padx=10, sticky='WE')

        content = tk.Label(frame, text='Mediana', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=1, column=3, padx=10, sticky='WE')

        content = tk.Label(frame, text='Moda', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=1, column=4, padx=10, sticky='WE')

        content = tk.Label(frame, text='Curtosis', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=1, column=5, padx=10, sticky='WE')

        content = tk.Label(frame, text='Oblicuidad', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=1, column=6, padx=10, sticky='WE')

        content = tk.Label(frame, text='Relación', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=1, column=7, padx=10, sticky='WE')

        # Label de encabezados laterales de la tabla

        content = tk.Label(frame, text='Longitud', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=2, column=1, padx=10, sticky='W')

        content = tk.Label(frame, text='Diametro', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=3, column=1, padx=10, sticky='W')

        content = tk.Label(frame, text='Altura', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=4, column=1, padx=10, sticky='W')

        content = tk.Label(frame, text='Peso completo', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=5, column=1, padx=10, sticky='W')

        content = tk.Label(frame, text='Peso de la concha', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=6, column=1, padx=10, sticky='W')

        content = tk.Label(frame, text='Peso de la víscera', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=7, column=1, padx=10, sticky='W')

        content = tk.Label(frame, text='Peso del caparazón', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=8, column=1, padx=10, sticky='W')

        content = tk.Label(frame, text='Número de anillos', bg='#faf9f9', font=('Segoe UI', 12))
        content.grid(row=9, column=1, padx=10, sticky='W')

        for i in range(1, len(self.dataSetObject.getColumns())):
            
            mean = round(self.dataSetObject.data[self.dataSetObject.getColumns()[i]].mean(),5)
            median = round(self.dataSetObject.data[self.dataSetObject.getColumns()[i]].median(),5)
            mode = round(self.dataSetObject.data[self.dataSetObject.getColumns()[i]].mode(),5)
            kurtosis = round(self.dataSetObject.data[self.dataSetObject.getColumns()[i]].kurtosis(),5)
            skewness = round(self.dataSetObject.data[self.dataSetObject.getColumns()[i]].skew(),5)

            for j in range(1, 7):

                content = tk.Label(frame, bg='#faf9f9', font=('Segoe UI', 12))
                content.grid(row=i+1, column=j+1, sticky='WE')
                relationship = ''

                if (j == 1):
                    content.config(text = mean)
                elif (j == 2):
                    content.config(text = median)
                elif (j == 3):
                    stringMode = ''
                    for k in mode:
                        stringMode += str(k) + ', '
                    content.config(text = stringMode[0:len(stringMode)-2])
                elif (j == 4):
                    content.config(text = kurtosis)
                elif (j == 5):
                    content.config(text = skewness)
                elif (j == 6):
                    if (mean == median and  median == mode[0]):
                        relationship = 'Distribución simétrica'
                    elif (mean > median):
                        relationship = 'Asimetría positiva'
                    elif (mean < median):
                        relationship = 'Asimetría negativa'
                    content.config(text = relationship)

        lbl = tk.Label(frame, text='Resumen estadístico', bg='#faf9f9', font=('Segoe UI', 18, 'bold'))
        lbl.grid(row=0, column=1, columnspan=7, sticky='WE', pady=5)  

        btnClose = tk.Button(frame, text="Cerrar", activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2', command=lambda: newgraphWindow.destroy(), font=('Segoe UI', 10))
        btnClose.grid(row=10, column=4, pady=10, sticky='E')

# Llamado a la accion de la aplicacion

if __name__ == "__main__":
    app = main()
    app.root.mainloop()