from bibliotecas.importacoes import *
from voz.config_voz import *

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def falar(texto):
    """Função que converte texto em fala."""
    engine.say(texto)
    engine.runAndWait()

def capturar_fala():
    """Captura a fala do usuário usando o microfone."""
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Aguardando o comando...")
            audio = recognizer.listen(source)
        return recognizer.recognize_google(audio, language='pt-BR')
    except sr.UnknownValueError:
        falar("Não consegui entender. Pode repetir?")
    except sr.RequestError:
        falar("Erro no serviço de reconhecimento. Tente novamente.")
    return None

def validar_cpf(cpf):
    """Valida se o CPF tem 11 dígitos e contém apenas números."""
    return cpf.isdigit() and len(cpf) == 11

def pedir_cpf():
    """Solicita o CPF ao usuário até que um CPF válido seja fornecido."""
    while True:
        falar("Por favor, informe seu CPF.")
        cpf = capturar_fala()
        if cpf and validar_cpf(cpf):
            return cpf
        falar("CPF inválido. Por favor, repita.")

def chamar_boleto(cpf):
    """Consulta o boleto do usuário a partir do CPF."""
    url = 'http://127.0.0.1:5000/suporte/faturamento'
    try:
        resposta = requests.post(url, json={'cpf': cpf})
        if resposta.status_code == 200:
            dados = resposta.json()
            falar(f"Boleto no valor de {dados['boleto']['valor']} com vencimento em {dados['boleto']['vencimento']}.")
        else:
            falar("Erro ao encontrar o boleto.")
    except Exception as e:
        print(f"Erro na consulta: {e}")
        falar("Erro ao consultar o boleto.")

def chamar_teste_velocidade(cpf):
    """Executa o teste de velocidade de conexão para o CPF fornecido."""
    url = 'http://127.0.0.1:5000/teste/velocidade'
    try:
        resposta = requests.post(url, json={'cpf': cpf})
        if resposta.status_code == 200:
            dados = resposta.json()
            falar(f"Download: {dados['velocidade']['download']}, Upload: {dados['velocidade']['upload']}, Ping: {dados['velocidade']['ping']}.")
        else:
            falar("Erro ao realizar o teste.")
    except Exception as e:
        print(f"Erro: {e}")
        falar("Erro ao realizar o teste de velocidade.")

def interagir_com_cliente():
    """Interage com o cliente, oferecendo suporte para boletos e teste de velocidade."""
    falar("Olá, sou o assistente da Octa. Como posso ajudar?")
    while True:
        falar("Diga 'boleto', 'teste de velocidade' ou 'sair'.")
        comando = capturar_fala()
        if comando:
            if "boleto" in comando.lower():
                cpf = pedir_cpf()
                chamar_boleto(cpf)
            elif "teste" in comando.lower():
                cpf = pedir_cpf()
                chamar_teste_velocidade(cpf)
            elif "sair" in comando.lower():
                falar("Obrigado. Até logo!")
                break
            else:
                falar("Não entendi, repita, por favor.")

if __name__ == "__main__":
    interagir_com_cliente()
