import requests
import pyttsx3
import speech_recognition as sr

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
            falar(f"Boleto no valor de {dados['boleto']['valor']} com vencimento em {dados['boleto']['vencimento']}.")
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
            falar(f"Velocidade de download: {dados['velocidade']['download']}, upload: {dados['velocidade']['upload']}, ping: {dados['velocidade']['ping']}.")
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
