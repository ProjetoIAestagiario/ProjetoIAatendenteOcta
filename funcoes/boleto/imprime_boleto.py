import pyttsx3
import speech_recognition as sr
import time

# Simula um banco de dados com dois clientes
clientes = [
    {"nome": "Marcos Kaynan",
     "cpf": "12345678900", 
     "valor_boleto": 120.50},

    {"cpf": "345", "nome": "Wendell Carlos", "valor_boleto": 89.99}
]

# Inicializa o motor de fala
texto_fala = pyttsx3.init()

def configurar_voz():
    """Configura a voz do assistente."""
    texto_fala.setProperty('rate', 205)  # Velocidade de fala
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice', voices[0].id)  # Voz masculina

def falar(texto):
    """ para converter o texto em fala."""
    texto_fala.say(texto)
    texto_fala.runAndWait()

def capturar_fala():
    """Captura a fala e converte para texto."""
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte_audio:
        try:
            falar("Estou ouvindo...")
            print("Ouvindo...")
            audio = reconhecedor.listen(fonte_audio)
            texto = reconhecedor.recognize_google(audio, language="pt-BR")
            print(f"Você falou: {texto}")
            return texto
        except sr.UnknownValueError:
            falar("Desculpe, não consegui entender. Por favor, tente novamente.")
            print("Erro: Não foi possível reconhecer a fala.")
        except sr.RequestError as e:
            falar("Erro ao se comunicar com o serviço de reconhecimento de fala.")
            print(f"Erro: {e}")
        return ""

def texto_para_numero(texto):
    """Converte números escritos em letras para formato numéricos, uma observação a se fazer durante as capturas de fala quando se trata de números."""
    mapa_numeros = {
        "um": "1", "dois": "2", "três": "3", "quatro": "4", "cinco": "5",
        "seis": "6", "sete": "7", "oito": "8", "nove": "9", "zero": "0"
    }
    for palavra, numero in mapa_numeros.items():
        texto = texto.replace(palavra, numero)
    return texto.replace(" ", "")  # Remove espaços das palavras para formar o número completo 

def buscar_boleto():
    """Busca o boleto de um cliente no banco de dados."""
    falar("Por favor, informe o seu CPF.")
    texto_falado = capturar_fala()
    cpf = texto_para_numero(texto_falado).replace(".", "").replace("-", "").strip()
    
    if not cpf:
        falar("Nenhum CPF foi informado. Tente novamente.")
        print("Erro: CPF não informado.")
        return

    cliente = next((c for c in clientes if c["cpf"] == cpf), None)
    if cliente:
        falar(f"Boleto encontrado para {cliente['nome']}. O valor é {cliente['valor_boleto']} reais.")
        print(f"Boleto encontrado para {cliente['nome']}. Valor: R$ {cliente['valor_boleto']:.2f}")
        falar("Gerando boleto, por favor, aguarde.")
        time.sleep(3)  # Tempo para simular a geração do boleto
        falar("O boleto foi gerado com sucesso.")
        print("O boleto foi gerado com sucesso.")
        falar("Por favor, dirija-se até um dos nossos atendentes para pegar o seu boleto.")
        print("Por favor, dirija-se até um dos nossos atendentes para pegar o seu boleto.")
    else:
        falar("Cliente não encontrado. Por favor, tente novamente.")
        print("Erro: Cliente não encontrado.")

def listar_clientes():
    """Lista todos os clientes cadastrados no banco de dados."""
    falar("Aqui estão todos os clientes cadastrados.")
    print("Lista de clientes cadastrados:")
    for cliente in clientes:
        print(f"Nome: {cliente['nome']}, CPF: {cliente['cpf']}, Valor do boleto: R$ {cliente['valor_boleto']:.2f}")

# Função principal
def main():
    configurar_voz()
    falar("Seja bem-vindo à Ócta Telecom, como posso ajudar?")
    print("Seja bem-vindo à Ócta Telecom, como posso ajudar?")
    
    while True:
        falar("Buscar boleto ou sair.")
        opcao = capturar_fala().lower()
        
        if "boleto" in opcao:
            buscar_boleto()
        elif "listar clientes" in opcao:
            listar_clientes()
        elif "sair" in opcao:
            falar("Obrigado por usar nossos serviços. Até logo!")
            print("Encerrando o sistema. Até logo!")
            break
        else:
            falar("Não entendi. Por favor, tente novamente.")
            print("Erro: Não entendi, tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
