import speech_recognition as sr
import subprocess as sub
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, colors
from pygame import mixer

name = "nala"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk (text):
    engine.say(text)
    engine.runAndWait()

def listen ():
    listener = sr.Recognizer()     
    with sr.Microphone() as source:
        print("Escuchando...")
        listener.adjust_for_ambient_noise(source)
        pc = listener.listen(source)

    try:
        rec = listener.recognize_google(pc, language="es")
        rec = rec.lower()
        if name in rec:
            rec = rec.replace(name, '')
    except sr.UnknownValueError:
        print("No te entendí, intenta de nuevo")
    return rec

def inicial():
     while True:
        try:
            rec = listen()
        except UnboundLocalError:
            print("No te entendí, intenta de nuevo")
            continue     
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo " + music)
            talk("Reproduciendo " + music)
            pywhatkit.playonyt(music)
        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 2)
            print(search + ": " + wiki)
            talk(wiki)
        elif 'alarma' in rec:
            alarm = rec.replace('alarma', '')
            alarm = alarm.strip()
            talk("Alarma activada a las " + alarm + " horas")
            while True:
                if datetime.gatetime.now().strftime('%H:%M') == alarm:
                    print("DESPIERTA CRRANO!!!!!!! ")
                    mixer.init()
                    mixer.music.load("Limpia Parabrisas - Daddy Yankee ( Con letra ).mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break
        elif 'colores' in rec:
            talk("Enseguida")
            colors.capture()
if __name__ == '__main__':
    inicial()