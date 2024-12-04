from bibliotecas.importacoes import *
from function.voz.voz import *
from assistente import *


def imprimir_boleto_cliente():

    while True:
        falar("Que que eu imprima o seu boleto?")
        comando = capturar_fala()

        if comando and "sim" in comando.lower():
            cpf = pedir_cpf()
            chamar_boleto(cpf)
        elif comando and "não" in comando.lower():
            cpf = pedir_cpf()
            chamar_teste_velocidade(cpf)
        elif comando and "sair" in comando.lower():
            falar("Obrigado por utilizar o assistente da Octa. Até logo!")
            break
        else:
            falar("Desculpe, não entendi. Por favor, repita sua solicitação.")