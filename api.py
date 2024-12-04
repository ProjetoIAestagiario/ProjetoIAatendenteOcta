# api
""" importação de todas as bibliotecas """
from bibliotecas.importacoes import *

app = Flask(__name__)

# Carregar dados fictícios de clientes


def carregar_clientes():
    with open('client_data.json', 'r') as file:
        return json.load(file)

# Função para confirmar os dados do cliente


def confirmar_dados(cpf):
    clientes = carregar_clientes()
    cliente = clientes.get(cpf)
    if cliente:
        return cliente
    return None

# Função para simular a consulta de boleto


def consultar_boleto(cpf):
    # Simula uma consulta de boleto
    return {
        "boleto": f"Seu boleto foi gerado com sucesso. CPF: {cpf}",
        "valor": f"R$ {random.randint(100, 500)}",
        "vencimento": f"{random.randint(1, 28):02d}/{random.randint(1, 12):02d}/2024"
    }

# Função para realizar o teste de velocidade


def realizar_teste_velocidade():
    # Simula um teste de velocidade
    download = random.randint(10, 100)
    upload = random.randint(5, 50)
    return {
        "download": f"{download} Mbps",
        "upload": f"{upload} Mbps",
        "ping": f"{random.randint(10, 50)} ms"
    }


@app.route('/suporte/tecnico', methods=['POST'])
def suporte_tecnico():
    dados = request.json
    cpf = dados.get('cpf')

    # Confirmação de dados
    cliente = confirmar_dados(cpf)
    if not cliente:
        return jsonify({"erro": "Hm... Não consegui encontrar o cliente. Pode verificar o CPF e tentar novamente?"}), 400

    return jsonify({"suporte": f"Ok... Suporte técnico iniciado para {cliente['nome']} (CPF: {cpf}). Estamos aqui para ajudar."}), 200


@app.route('/suporte/faturamento', methods=['POST'])
def suporte_faturamento():
    dados = request.json
    cpf = dados.get('cpf')

    # Confirmação de dados
    cliente = confirmar_dados(cpf)
    if not cliente:
        return jsonify({"erro": "Ops... Não encontrei esse cliente. Tem certeza de que o CPF está correto?"}), 400

    boleto = consultar_boleto(cpf)
    return jsonify({
        "suporte": f"Entendido... Estamos iniciando a emissão da segunda via para {cliente['nome']} (CPF: {cpf}).",
        "boleto": boleto
    }), 200


@app.route('/suporte/instalacao', methods=['POST'])
def suporte_instalacao():
    dados = request.json
    cpf = dados.get('cpf')

    # Confirmação de dados
    cliente = confirmar_dados(cpf)
    if not cliente:
        return jsonify({"erro": "Hum... Cliente não encontrado. Pode confirmar os dados, por favor?"}), 400

    return jsonify({"suporte": f"Certo... Agendamento de instalação registrado para {cliente['nome']} (CPF: {cpf})."}), 200


@app.route('/teste/velocidade', methods=['POST'])
def teste_velocidade():
    dados = request.json
    cpf = dados.get('cpf')

    # Confirmação de dados
    cliente = confirmar_dados(cpf)
    if not cliente:
        return jsonify({"erro": "Hm... Não encontrei esse CPF no sistema. Poderia verificar os dados?"}), 400

    velocidade = realizar_teste_velocidade()
    return jsonify({
        "suporte": f"Beleza... Teste de velocidade concluído para {cliente['nome']} (CPF: {cpf}). Aqui estão os resultados:",
        "velocidade": velocidade
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
