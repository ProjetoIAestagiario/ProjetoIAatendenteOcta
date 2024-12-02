# assistente.py

import speech_recognition as sr
import pyttsx3
import requests

# Inicialização do reconhecimento de fala e da síntese de voz
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Função para falar com o cliente


def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# Função para capturar a fala do cliente com verificação de microfone


def capturar_fala():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Aguardando o comando...")
            audio = recognizer.listen(source)
        comando = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando
    except sr.UnknownValueError:
        print("Não entendi, por favor, repita.")
        falar("Não entendi, por favor, repita.")
        return capturar_fala()
    except sr.RequestError:
        print("Erro ao acessar o serviço de reconhecimento de fala.")
        falar("Erro ao acessar o serviço de reconhecimento de fala.")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        falar("Ocorreu um erro inesperado.")
        return None

# Função para pedir o CPF e validar


def pedir_cpf():
    falar("Por favor, informe seu CPF.")
    cpf = capturar_fala()
    return cpf

# Função para chamar a API para consulta de boleto


def chamar_boleto(cpf):
    url = 'http://127.0.0.1:5000/suporte/faturamento'
    try:
        resposta = requests.post(url, json={'cpf': cpf})
        if resposta.status_code == 200:
            dados = resposta.json()
            print(dados["suporte"])
            print(f"Boleto: {dados['boleto']['valor']} com vencimento em {
                  dados['boleto']['vencimento']}")
            falar(f"Boleto de valor {dados['boleto']['valor']} com vencimento em {
                  dados['boleto']['vencimento']}.")
        else:
            erro = resposta.json().get('erro', 'Erro desconhecido.')
            print(erro)
            falar(erro)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao se comunicar com a API: {e}")
        falar("Erro ao se comunicar com o servidor. Tente novamente mais tarde.")
    except ValueError:
        print("Resposta inválida do servidor.")
        falar("Houve um problema com a resposta do servidor.")

# Função para realizar o teste de velocidade


def chamar_teste_velocidade(cpf):
    url = 'http://127.0.0.1:5000/teste/velocidade'
    resposta = requests.post(url, json={'cpf': cpf})

    if resposta.status_code == 200:
        dados = resposta.json()
        print(dados["suporte"])
        print(f"Download: {dados['velocidade']['download']}, Upload: {
              dados['velocidade']['upload']}, Ping: {dados['velocidade']['ping']}.")
        falar(f"Download: {dados['velocidade']['download']}, Upload: {
              dados['velocidade']['upload']}, Ping: {dados['velocidade']['ping']}.")
    else:
        print(resposta.json()['erro'])
        falar(resposta.json()['erro'])

# Função principal para interação com o cliente


def interagir_com_cliente():
    falar("Olá, eu sou o assistente virtual da ÓctaTelecom. Como posso te ajudar hoje?")

    while True:
        falar("Para suporte, diga boleto ou teste de velocidade. Para encerrar, diga sair.")
        comando = capturar_fala()

        if comando and "boleto" in comando.lower():
            cpf = pedir_cpf()
            chamar_boleto(cpf)
        elif comando and "teste" in comando.lower():
            cpf = pedir_cpf()
            chamar_teste_velocidade(cpf)
        elif comando and "sair" in comando.lower():
            falar("Obrigado por utilizar o assistente da Octa. Até logo!")
            break
        else:
            falar("Desculpe, não entendi. Por favor, repita sua solicitação.")


# Iniciar o assistente
if __name__ == "__main__":
    interagir_com_cliente()

# Inicialização
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def falar(texto):
    """Fala o texto fornecido."""
    engine.say(texto)
    engine.runAndWait()


def capturar_fala():
    """Captura e retorna a fala do usuário."""
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Aguardando o comando...")
            audio = recognizer.listen(source)
        comando = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando
    except sr.UnknownValueError:
        falar("Não consegui entender. Pode repetir?")
        return capturar_fala()
    except sr.RequestError:
        falar("Erro no serviço de reconhecimento. Tente novamente mais tarde.")
        return None
    except Exception as e:
        falar("Ocorreu um erro inesperado.")
        print(f"Erro: {e}")
        return None


def validar_cpf(cpf):
    """Valida a estrutura do CPF (básico, não verifica autenticidade)."""
    return cpf.isdigit() and len(cpf) == 11


def pedir_cpf():
    """Solicita e retorna um CPF válido."""
    while True:
        falar("Por favor, informe seu CPF.")
        cpf = capturar_fala()
        if cpf and validar_cpf(cpf):
            return cpf
        else:
            falar("CPF inválido. Por favor, diga apenas os 11 dígitos do CPF.")


def chamar_boleto(cpf):
    """Consulta o boleto pelo CPF."""
    try:
        url = 'http://127.0.0.1:5000/suporte/faturamento'
        resposta = requests.post(url, json={'cpf': cpf})

        if resposta.status_code == 200:
            dados = resposta.json()
            falar(f"Boleto no valor de {dados['boleto']['valor']} com vencimento em {
                  dados['boleto']['vencimento']}.")
        else:
            falar("Não foi possível encontrar o boleto. Verifique os dados.")
    except Exception as e:
        print(f"Erro na consulta de boleto: {e}")
        falar("Ocorreu um erro ao consultar o boleto.")


def chamar_teste_velocidade(cpf):
    """Realiza o teste de velocidade."""
    try:
        url = 'http://127.0.0.1:5000/teste/velocidade'
        resposta = requests.post(url, json={'cpf': cpf})

        if resposta.status_code == 200:
            dados = resposta.json()
            falar(f"Velocidade de download: {dados['velocidade']['download']}, upload: {
                  dados['velocidade']['upload']}, ping: {dados['velocidade']['ping']}.")
        else:
            falar("Não foi possível realizar o teste de velocidade.")
    except Exception as e:
        print(f"Erro no teste de velocidade: {e}")
        falar("Ocorreu um erro ao realizar o teste de velocidade.")


def interagir_com_cliente():
    """Interação principal com o cliente."""
    falar("Olá, sou o assistente da Octa. Como posso te ajudar?")

    while True:
        falar("Diga 'boleto', 'teste de velocidade' ou 'sair'.")
        comando = capturar_fala()

        if comando and "boleto" in comando.lower():
            cpf = pedir_cpf()
            if cpf:
                chamar_boleto(cpf)
        elif comando and "teste" in comando.lower():
            cpf = pedir_cpf()
            if cpf:
                chamar_teste_velocidade(cpf)
        elif comando and "sair" in comando.lower():
            falar("Obrigado por usar o assistente Octa. Até logo!")
            break
        else:
            falar("Não entendi. Pode repetir, por favor?")


if __name__ == "__main__":
    interagir_com_cliente()
