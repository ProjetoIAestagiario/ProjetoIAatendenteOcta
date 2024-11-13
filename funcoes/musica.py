# Funções relacionadas à música (tocar música)
import webbrowser


def tocar_musica(falar_func, ouvir_comando_func):
    """Toca uma música no YouTube baseada no comando do usuário."""
    falar_func("Qual música você gostaria de ouvir?")
    musica = ouvir_comando_func()
    if musica:
        falar_func(f"Tocando {musica} no YouTube.")
        webbrowser.open(
            f"https://www.youtube.com/results?search_query={musica}")
    else:
        falar_func("Desculpe, não entendi o nome da música.")
