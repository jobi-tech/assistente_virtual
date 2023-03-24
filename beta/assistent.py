import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
from PySimpleGUI import PySimpleGUI as sg

rec = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Ouvindo...")
        audio = rec.listen(mic)
        comando = rec.recognize_google(audio, language="pt-BR")
        comando = comando.lower()
        if 'beta' in comando:
            comando = comando.replace('beta', '')
            #maquina.say(comando)
            maquina.runAndWait()

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()

    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()

    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt((musica))
        maquina.say('Tocando música')
        maquina.runAndWait()


comando_voz_usuario()






# ------------------------- ESSA ARROMBADA FOI CRIADA PELO JOSUÉ FERREIRA RIBEIRO :3, TRATE BEM DELA ------------------- #




