import pyttsx3
import datetime
import speech_recognition as sr
from datetime import datetime

texto_fala = pyttsx3.init()


def falar(audio): #função responsável por transformar texto em fala 
    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty('rate',170) #alteração da velocidade da voz
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice',voices[0].id) #alteração da voz
    texto_fala.say(audio)
    texto_fala.runAndWait()


def tempo():
    data_e_hora_atuais = datetime.now()
    Tempo = data_e_hora_atuais.strftime('%H:%M')
    falar('Agora são: ')
    falar(Tempo)
    print(Tempo)

def data():
    data_do_dia_de_hoje = datetime.now()
    Data = data_do_dia_de_hoje.strftime('%d/%m/%Y')
    falar('A data de hoje é: ')
    falar(Data)
    falar('Ócto a sua disposição, como posso ajudá-lo')
    
def bem_vindo():

    hora = datetime.now().hour
    if hora >= 6 and hora <12:
        falar('Bom dia mestre!')
    elif hora >= 12 and hora <18:
        falar('Boa tarde mestre')
    elif hora >= 18 and hora <=24:
        falar('Boa noite mestre')
    else:
        falar('Bom dia mestre Wendell!')

def microphone():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Reconhecendo...')
        comando = r.recognize_google(audio,language='pt-BR')
        print(comando)
    except Exception as e:
        print(e)
        falar('Por favor repita!')

        return "None"

    return comando

bem_vindo()
tempo()
data()
microphone()