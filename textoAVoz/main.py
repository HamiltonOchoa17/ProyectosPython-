from gtts import gTTS

import os

texto = "Hola Mundo"

output = gTTS(texto, lang='es', slow=False)
output.save("output.mp3")

os.system('cvlc output.mp3')