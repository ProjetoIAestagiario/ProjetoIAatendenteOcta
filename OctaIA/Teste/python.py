import speech_recognition as sr
import pyttsx3

# Inicializar o sintetizador de voz
motor_fala = pyttsx3.init()
motor_fala.setProperty('rate', 200)  # Define a velocidade para menos robotizada

# Tenta definir uma voz masculina em português
for voz in motor_fala.getProperty('voices'):
    if 'portuguese' in voz.languages and 'male' in voz.name.lower():
        motor_fala.setProperty('voice', voz.id)
        break
    elif 'brazil' in voz.id and 'male' in voz.name.lower():
        motor_fala.setProperty('voice', voz.id)
        break

# Nome do assistente
nome_assistente = "octo"

# Função para o assistente falar
def falar(texto):
    motor_fala.say(texto)
    motor_fala.runAndWait()

# Função para escolher entre falar ou digitar usando um menu apenas na primeira interação
def escolher_entrada():
    falar("Escolha como deseja interagir comigo.")
    print("\n=== Menu de Entrada ===")
    print("1. Falar o comando")
    print("2. Digitar o comando")
    escolha = input("Escolha uma opção (1 ou 2): ")

    if escolha == "1":
        return ouvir_comando()  # Volta para escuta de comando por voz
    elif escolha == "2":
        comando = input("Digite o comando: ")
        return comando.lower()
    else:
        falar("Escolha inválida. Tente novamente.")
        return ""

# Função para ouvir e reconhecer o comando de voz
def ouvir_comando():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte:
        print("Ouvindo...")
        reconhecedor.adjust_for_ambient_noise(fonte)
        audio = reconhecedor.listen(fonte)

        try:
            comando = reconhecedor.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            falar("Erro ao conectar ao serviço de reconhecimento de voz.")
            return ""

# Função para mostrar o menu de opções
def mostrar_menu():
    opcoes = [
        "1. Consultar saldo e faturas",
        "2. Relatar problema de conexão",
        "3. Agendar visita técnica",
        "4. Alterar plano de internet",
        "5. Falar com um atendente",
        "6. Encerrar atendimento"
    ]
    falar("Em que posso ajudar?")
    for opcao in opcoes:
        print(opcao)
        falar(opcao)

# Função para processar o comando e responder ao usuário
def processar_comando(comando):
    if "consultar saldo" in comando or "faturas" in comando or comando == "1":
        falar("Acessando a área de saldo e faturas.")
    elif "relatar problema" in comando or "conexão" in comando or comando == "2":
        falar("Entendo, vamos relatar o problema de conexão.")
    elif "visita técnica" in comando or comando == "3":
        falar("Certo, vamos agendar uma visita técnica.")
    elif "alterar plano" in comando or comando == "4":
        falar("Vamos alterar o plano de internet.")
    elif "falar com atendente" in comando or comando == "5":
        falar("Conectando com um atendente.")
    elif "encerrar" in comando or comando == "6":
        falar("Encerrando atendimento. A OctaTelecom agradece!")
        return False
    else:
        falar("Opção não reconhecida. Por favor, tente novamente.")
    return True

# Função principal do assistente
def principal():
    falar(f"Olá, eu sou {nome_assistente.capitalize()}, assistente virtual da OctaTelecom. Se precisa de ajuda, chame meu nome {nome_assistente.capitalize()}, se precisar de ajuda. Agora em que posso ajudar?")

    # Primeira interação para escolher entre digitar ou falar
    comando = escolher_entrada()

    # Se o nome do assistente for mencionado, mostrar o menu uma vez
    if nome_assistente in comando:
        mostrar_menu()

        # Loop para receber comandos a partir do menu de opções diretamente
        while True:
            comando = input("Escolha uma opção ou digite seu comando: ").lower()
            if not processar_comando(comando):
                break

principal()
