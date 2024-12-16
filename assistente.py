from bibliotecas.importacoes import *
from function.voz.voz import *
from function.hora_data import *


def validar_cpf(cpf):
    """Valida se o CPF tem 11 dígitos e contém apenas números."""
    return cpf.isdigit() and len(cpf) == 4


def pedir_cpf():
    """Solicita o CPF ao usuário até que um CPF válido seja fornecido."""
    while True:
        falar("Certo, agora... por favor, informe o seu CPF.")
        cpf = capturar_fala()
        if cpf and validar_cpf(cpf):
            return cpf
        falar("Hum, parece que o CPF informado está inválido. Pode tentar novamente?")


def chamar_boleto(cpf):
    """Consulta o boleto do usuário a partir do CPF."""
    url = 'http://127.0.0.1:5000/suporte/faturamento'
    try:
        resposta = requests.post(url, json={'cpf': cpf})
        if resposta.status_code == 200:
            dados = resposta.json()
            falar(
                f"Aqui está: o boleto é no valor de {dados['boleto']['valor']} e vence em {dados['boleto']['vencimento']}. Espero que isso ajude!"
            )
        else:
            falar("Hmm, parece que houve um problema para encontrar o seu boleto. Pode tentar novamente mais tarde?")
    except Exception as e:
        print(f"Erro na consulta: {e}")
        falar("Infelizmente, ocorreu um erro ao consultar o boleto. Tente novamente mais tarde.")


def chamar_teste_velocidade(cpf):
    """Executa o teste de velocidade de conexão para o CPF fornecido."""
    url = 'http://127.0.0.1:5000/teste/velocidade'
    try:
        resposta = requests.post(url, json={'cpf': cpf})
        if resposta.status_code == 200:
            dados = resposta.json()
            falar(
                f"Tudo certo! Olha só: sua velocidade de download está em {dados['velocidade']['download']}, upload em {dados['velocidade']['upload']} e o ping está em {dados['velocidade']['ping']}. Espero que isso ajude!"
            )
        else:
            falar("Poxa, não consegui realizar o teste agora. Pode tentar mais tarde?")
    except Exception as e:
        print(f"Erro: {e}")
        falar("Ocorreu um problema ao realizar o teste de velocidade. Tente novamente mais tarde.")


def interagir_com_cliente():
    """Interage com o cliente, oferecendo suporte para boletos e teste de velocidade."""
    #saudacao_cliente() #tenho que tentar adiciona essa funcão aqui.


    while True:
        #falar("Se precisar, diga 'boleto', 'teste de velocidade' ou 'sair'. Estou aqui para ajudar.")
        comando = capturar_fala()
        if comando:
            if "boleto" in comando.lower():
                cpf = pedir_cpf()
            elif "teste" in comando.lower():
                cpf = pedir_cpf()
                chamar_teste_velocidade(cpf)
            elif "sair" in comando.lower():
                falar(
                    "Certo, obrigado por utilizar o assistente da Ócta. Até a próxima!")
                break
            else:
                falar(
                    "Desculpe, não entendi bem o que você quis dizer. Pode repetir, por favor?")


if __name__ == "__main__":
    interagir_com_cliente()
