import os
from tkinter import  Tk, Text,  Button, END, Label
from gtts import gTTS


def saveTxt():
    text =  textArea.get("1.0", END)  # Los parametros 1.0  son (linea.columna) del texto esta END final del texto
    with open('demo.txt', 'w', encoding='utf-8') as file:
        file.write(text)
    statusLabel.configure(text='Texto guardado con exito')



def playTxt():
    text = textArea.get("1.0", END)
    speech =  gTTS(text=text, lang='es', slow=False)
    speech.save('output.pm3')

    os.system('cvlc output.mp3')
#Crear la venta principal

root =  Tk()
root.title("Texto a voz")

textArea = Text(root, height=10, width=50)
textArea.pack()

saveButton = Button(root, text='Gurdar Texto', command=saveTxt)
saveButton.pack()


playButton = Button(root, text='Reproducir Texto', command=playTxt)
playButton.pack()


statusLabel = Label(root, text="", fg='green')
statusLabel.pack()


root.mainloop()
