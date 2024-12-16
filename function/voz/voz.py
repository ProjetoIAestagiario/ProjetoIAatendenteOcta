from bibliotecas.importacoes import *
from function.voz.voz import *

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def falar(texto):
    """Função que converte texto em fala."""
    engine.say(texto)
    engine.runAndWait()


def capturar_fala():
    """Captura a fala do usuário usando o microfone."""
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            #falar("Estou ouvindo, pode falar.")
            print("Estou ouvindo...")
            audio = recognizer.listen(source)
        return recognizer.recognize_google(audio, language='pt-BR')
    except sr.UnknownValueError:
        falar("Não consegui entender. Pode repetir?")
    except sr.RequestError:
        falar("Erro no serviço de reconhecimento. Tente novamente.")
    return None


""" def capturar_comando_durante_fala(texto):
    #Verifica se há uma interrupção enquanto o assistente fala.
    def ouvir_interrupcao():
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Verificando interrupção...")
                audio = recognizer.listen(
                    source, timeout=3, phrase_time_limit=3)
            return recognizer.recognize_google(audio, language='pt-BR')
        except Exception:
            return None

    engine.say(texto)
    engine.startLoop(False)
    while engine.isBusy():
        comando_interrupcao = ouvir_interrupcao()
        if comando_interrupcao:
            engine.endLoop()
            return comando_interrupcao
    engine.endLoop()
    return None
 """
