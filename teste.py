import random
import speech_recognition as sr
import pyttsx3

# Inicializa o motor de síntese de fala
engine = pyttsx3.init()

def falar(texto):
    """Função para o assistente falar de volta ao usuário."""
    engine.say(texto)
    engine.runAndWait()

def ouvir():
    """Função para ouvir o que o usuário está dizendo."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando comando...")
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        falar("Desculpe, não consegui entender o que você disse.")
        return None
    except sr.RequestError:
        falar("Desculpe, houve um erro ao tentar reconhecer sua fala.")
        return None

def imprimir_boleto(cliente_nome, valor_boleto):
    """Simula a impressão de um boleto para o cliente."""
    falar(f"Imprimindo boleto para {cliente_nome} no valor de R${valor_boleto:.2f}")
    print(f"\nBoleto - Provedora de Internet")
    print(f"Cliente: {cliente_nome}")
    print(f"Valor: R$ {valor_boleto:.2f}")
    print(f"Vencimento: 10/12/2024")
    print("=====================================")
    print("Boleto gerado com sucesso!\n")

def consultar_plano():
    """Simula a consulta de planos disponíveis."""
    planos = ["Plano Básico: 50Mbps", "Plano Intermediário: 100Mbps", "Plano Avançado: 200Mbps"]
    falar("Aqui estão os planos disponíveis para você:")
    for plano in planos:
        print(f"- {plano}")
        falar(plano)
    print()

def consultar_faturas():
    """Simula a consulta de faturas."""
    faturas = [random.randint(80, 150) for _ in range(3)]  # Valores aleatórios
    falar("Aqui estão suas últimas faturas:")
    for i, fatura in enumerate(faturas, start=1):
        print(f"Fatura {i}: R$ {fatura:.2f}")
        falar(f"Fatura {i}: R$ {fatura:.2f}")
    print()

def suporte_tecnico():
    """Simula o suporte técnico."""
    falar("Você escolheu Suporte Técnico. Por favor, descreva seu problema.")
    problema = ouvir()
    if problema:
        falar(f"Estamos analisando o problema: {problema}. Nossa equipe de suporte entrará em contato com você em breve.\n")

def exibir_menu():
    """Exibe o menu de opções e escuta o comando do usuário."""
    falar("Bem-vindo ao assistente da Provedora de Internet!")
    falar("Escolha uma opção para continuar: ")
    falar("1. Consultar plano de internet.")
    falar("2. Imprimir boleto.")
    falar("3. Consultar faturas.")
    falar("4. Suporte técnico.")
    falar("5. Sair.")
    
def main():
    """Função principal que controla o fluxo do assistente de voz."""
    while True:
        exibir_menu()
        comando = ouvir()

        if comando:
            if "consultar plano" in comando:
                consultar_plano()
            elif "imprimir boleto" in comando:
                falar("Qual o seu nome, por favor?")
                cliente_nome = ouvir()
                if cliente_nome:
                    valor_boleto = random.uniform(50.0, 200.0)  # Valor aleatório para o boleto
                    imprimir_boleto(cliente_nome, valor_boleto)
            elif "consultar faturas" in comando:
                consultar_faturas()
            elif "suporte técnico" in comando:
                suporte_tecnico()
            elif "sair" in comando:
                falar("Saindo do assistente. Até logo!")
                break
            else:
                falar("Desculpe, não entendi essa opção. Tente novamente.")
        else:
            break

if __name__ == "__main__":
    main()
