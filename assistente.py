import requests
import pyttsx3
import speech_recognition as sr

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
    resposta = requests.post(url, json={'cpf': cpf})

    if resposta.status_code == 200:
        dados = resposta.json()
        print(dados["suporte"])
        print(f"Boleto: {dados['boleto']['valor']} com vencimento em {dados['boleto']['vencimento']}")
        falar(f"Boleto de valor {dados['boleto']['valor']} com vencimento em {dados['boleto']['vencimento']}.")
    else:
        print(resposta.json()['erro'])
        falar(resposta.json()['erro'])

# Função para realizar o teste de velocidade
def chamar_teste_velocidade(cpf):
    url = 'http://127.0.0.1:5000/teste/velocidade'
    resposta = requests.post(url, json={'cpf': cpf})

    if resposta.status_code == 200:
        dados = resposta.json()
        print(dados["suporte"])
        print(f"Download: {dados['velocidade']['download']}, Upload: {dados['velocidade']['upload']}, Ping: {dados['velocidade']['ping']}.")
        falar(f"Download: {dados['velocidade']['download']}, Upload: {dados['velocidade']['upload']}, Ping: {dados['velocidade']['ping']}.")
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
