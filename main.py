# main.py
import time
from funcoes.voz import configurar_voz, falar
from funcoes.util import ouvir_comando, informar_hora, informar_data
from funcoes.musica import tocar_musica
from funcoes.saudacao import saudacao_inicial


def perguntar_mais_ajuda():
    """Pergunta ao usuário se ele precisa de mais ajuda."""
    falar("Posso ajudar em mais alguma coisa?")
    resposta = ouvir_comando()
    if "sim" in resposta or "ajuda" in resposta:
        falar("Claro! Como posso ajudar?")
    else:
        falar("Ok, estarei aqui caso precise de mim.")


def responder_chamada():
    """Responde quando o assistente é chamado."""
    respostas = [
        "Sim, como posso ajudar?",
        "Oi, me chamou?",
        "Estou aqui, no que posso ajudar?",
        "Olá, posso ajudar em algo?"
    ]
    falar(respostas[int(time.time()) % len(respostas)])
    resposta = ouvir_comando()
    if not resposta:
        falar(
            "Parece que você me chamou, mas não respondeu. Estou aqui caso precise de algo!")


def atendimento():
    """Função principal de atendimento."""
    configurar_voz()
    saudacao_inicial(falar)  # Apresentação inicial

    while True:
        comando = ouvir_comando()

        if "marco" in comando:
            responder_chamada()
        elif "ajuda" in comando or "suporte" in comando:
            falar("Estou aqui para ajudar! Diga o que precisa.")
            perguntar_mais_ajuda()
        elif "hora" in comando:
            informar_hora(falar)
            perguntar_mais_ajuda()
        elif "data" in comando:
            informar_data(falar)
            perguntar_mais_ajuda()
        elif "tocar música" in comando:
            tocar_musica(falar, ouvir_comando)
            perguntar_mais_ajuda()
        elif "encerrar" in comando:
            falar(
                "Encerrando o atendimento. A OctaTelecom agradece sua companhia. Até logo!")
            break

def limpar_recursos():
    print("Limpando recursos antes de sair...")

def main():
    try:
        atendimento()  # Chama a função principal de atendimento
    except KeyboardInterrupt:
        print("\nOperação interrompida.")
        limpar_recursos()
        print("Programa encerrado com sucesso.")

if __name__ == '__main__':
    main()  # Executa a função principal


