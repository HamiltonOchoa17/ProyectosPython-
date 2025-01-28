import tkinter as tk
from tkinter import ttk  ## Es un modulo que proporciona widgest con estilos modernos de tkinter
from tkinter.ttk import Style

 ## Funciones de Barras
def incrementarBarra():
    valor = barraProgreso['value']
    if valor < 100:
        barraProgreso['value'] = valor + 10
        actualizarPorcentaje()

def completarBarra():
    valor = barraProgreso['value']
    if valor < 100:
        barraProgreso['value'] = valor + 5
        actualizarPorcentaje()
        ventana. after(100, completarBarra)

def resetearBarra():
    barraProgreso['value'] = 0
    actualizarPorcentaje()

def actualizarPorcentaje():
    valor = barraProgreso['value']
    porcentaje.set(f'{int(valor)}')

# ## Funciones de Barras

ventana = tk.Tk()
ventana.title('Barra de progreso')
ventana.geometry('300x250')
ventana.configure(bg='#2C3E50')


# Estilo para la barra de progreso y los botones
style = ttk.Style()
style.theme_use('alt')

#Estilo para barra de progreso

style.configure("TProgressbar",troughcolor='#34495E', background='#1ABC9C', thickness=20 )

# Estilo ara botones

style.configure("TButton", font=('Helvetica', 10, 'bold'), background='#2980B9', foreground='white')
style.map("TButton", background=[('active','#3498DB')])

barraProgreso = ttk.Progressbar(ventana, orient='horizontal', length=250, mode='determinate', style='TProgressbar')

barraProgreso.pack(pady=20)

porcentaje = tk.StringVar()
porcentaje.set('0%')

etiquetaPorcentaje = tk.Label(ventana, textvariable=porcentaje,
                              font=('Helvetica', 10, 'bold'), bg='#2C3E50', fg='white')
etiquetaPorcentaje.pack(pady=10)




botonIncrementar = ttk.Button(ventana, text='Incremntar', command= incrementarBarra, style="TButton")
botonIncrementar.pack(pady=5)

botonCompletar = ttk.Button(ventana, text='Completar', command= completarBarra, style="TButton")
botonCompletar.pack(pady=5)

botonResetear = ttk.Button(ventana, text='Resetear', command= resetearBarra , style="TButton")
botonResetear.pack(pady=20)




ventana.mainloop()







