# Funções relacionadas à saudação inicial
import datetime


def saudacao_inicial(falar_func):
    """Faz uma saudação inicial com base no horário."""
    hora = datetime.datetime.now().hour
    if 6 <= hora < 12:
        falar_func("Bom dia! Eu sou Ócto, o assistente virtual da OctaTelecom.")
    elif 12 <= hora < 18:
        falar_func("Boa tarde! Eu sou Ócto, o assistente virtual da OctaTelecom.")
    else:
        falar_func("Boa noite! Eu sou Ócto, o assistente virtual da OctaTelecom.")

    falar_func(
        "Estou aqui para ajudar com qualquer dúvida ou suporte relacionado aos nossos serviços de internet.")
    falar_func(
        "Posso informar sobre o status da sua fatura e verificar a conexão.")
    falar_func(
        "Estou pronto para ajudar sempre que precisar. Basta dizer 'Ócto' para que eu escute e responda!")
