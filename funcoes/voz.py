# core/voz.py
import pyttsx3

# Inicializa o motor de fala
texto_fala = pyttsx3.init()


def configurar_voz():
    """Configura a voz do assistente."""
    texto_fala.setProperty('rate', 220)  # Velocidade de fala
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice', voices[0].id)  # Voz masculina


def falar(texto):
    """Converte o texto em fala."""
    texto_fala.say(texto)
    texto_fala.runAndWait()
