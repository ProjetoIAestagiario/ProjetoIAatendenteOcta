from funcoes.voz import configurar_voz, falar


def imprimir_boleto(cliente_nome, valor_boleto):
    """Simula a impressão de um boleto para o cliente."""
    falar(f"Imprimindo boleto para {
          cliente_nome} no valor de R${valor_boleto:.2f}")
    print(f"\nBoleto - Provedora de Internet")
    print(f"Cliente: {cliente_nome}")
    print(f"Valor: R$ {valor_boleto:.2f}")
    print(f"Vencimento: 10/12/2024")
    print("=====================================")
    print("Boleto gerado com sucesso!\n")
