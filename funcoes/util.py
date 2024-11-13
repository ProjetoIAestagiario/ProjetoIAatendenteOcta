# Funções utilitárias como ouvir comandos, hora e data
import datetime
import speech_recognition as sr


def informar_hora(falar_func):
    """Informa a hora atual ao usuário."""
    hora_atual = datetime.datetime.now().strftime("%H:%M")
    falar_func(f"A hora atual é {hora_atual}.")


def informar_data(falar_func):
    """Informa a data atual ao usuário."""
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
    falar_func(f"A data de hoje é {data_atual}.")


def ouvir_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            print("Escutando...")
            audio = recognizer.listen(source, timeout=30, phrase_time_limit=10)
            comando = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Comando reconhecido: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("Não entendi o comando.")
            return ""
        except sr.RequestError:
            print("Erro de conexão com o Google Speech API.")
            return ""
        except sr.WaitTimeoutError:
            print("Tempo de escuta expirou. Tente novamente.")
            return ""
