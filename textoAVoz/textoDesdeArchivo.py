from gtts import gTTS
import os


with open('demo.txt', 'r', encoding='utf-8') as file:
    texto = file.read()


output = gTTS(texto, lang='es', slow=False)
output.save("output.mp3")

os.system('cvlc output.mp3')