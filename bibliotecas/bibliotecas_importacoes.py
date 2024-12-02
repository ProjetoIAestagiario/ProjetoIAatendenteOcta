import speech_recognition as sr
import pygame
import os

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microfone {index}: {name}")

# Inicializar o mixer de áudio
pygame.mixer.init()

# Função para reproduzir áudio
def reproduzir_audio(caminho_arquivo):
    if os.path.isfile(caminho_arquivo):
        pygame.mixer.music.load(caminho_arquivo)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
    else:
        print(f"Arquivo de áudio não encontrado: {caminho_arquivo}")

# Função para ouvir comando
def ouvir_comando():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Estou ouvindo...")
            audio = recognizer.listen(source, timeout=5)
            comando = recognizer.recognize_google(audio, language="pt-BR")
            return comando.lower()
    except sr.UnknownValueError:
        return "Não entendi."
    except sr.RequestError:
        return "Erro no serviço de reconhecimento."
    except sr.WaitTimeoutError:
        return "Tempo esgotado para escuta."
    except OSError as e:
        print(f"Erro no microfone: {e}")
        return "Erro ao acessar o microfone."

