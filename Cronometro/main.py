import tkinter as tk

#region clase cronometro
class Cronometro:



    # Iniciar



    def  __init__(self, master):
        self.master = master
        self.horas =  0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.corriendo = False   # Mientras la funciona sea True el cornometro corre
        self.display = tk.StringVar()
        self.actualizarDisplay("00:00:00.000")


        # Configuracion de la interfaz grafica
        self.master.title("Cronometro")
        self.master.configure(bg='#34495e')
        self.master.geometry("300x200")
        self.displayLabel = tk.Label(master, textvariable=self.display,
                                     font=('Arial',36), bg='#34495e',
                                     fg='#ffffff')

        self.displayLabel.pack()
        self.buttonFrame = tk.Frame(master, bg="#ffffff")
        self.buttonFrame.pack()

        #Botones inicio
        self.startButton =  tk.Button(self.buttonFrame, text='Inciar',
                                      command=self.iniciar, bg="#2ecc71",
                                      fg="#ffffff")
        self.startButton.pack(side=tk.LEFT, padx=5, pady=10)

        self.stopButton = tk.Button(self.buttonFrame, text='Pausar',
                                     command=self.detener, bg="#e74c4c",
                                     fg="#ffffff")
        self.stopButton.pack(side=tk.RIGHT, padx=5, pady=10)


        self.resetButton = tk.Button(self.buttonFrame, text='Reiniciar',
                                     command=self.reiniciar, bg="#3498db",
                                     fg="#ffffff")
        self.resetButton.pack(side=tk.LEFT, padx=5, pady=10)

    def iniciar(self):
        if not self.corriendo:
            self.corriendo = True
            self.actualizarCronometro()

    # Detener
    def detener(self):
        self.corriendo = False



    def actualizarDisplay(self, tiempo):
        self.display.set(tiempo)
    # Reiniciar

    def reiniciar(self):
        self.hora = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.actualizarDisplay("00:00:00.000")

    def actualizarCronometro(self):
        if self.corriendo:
            self.milisegundos += 10
            if self.milisegundos >= 1000:
                self.milisegundos = 0
                self.segundos += 1
            if self.segundos >= 60:
                self.segundos = 0
                self.minutos += 1
            if self.minutos >= 60:
                self.minutos = 0
                self.horas += 1

            tiempoFormateado = f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}.{self.milisegundos:03}"
            self.actualizarDisplay(tiempoFormateado)
            self.master.after(10, self.actualizarCronometro)
            #endregion
# endregion

if __name__  == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()


