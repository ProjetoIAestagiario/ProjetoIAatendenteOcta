# api

import time
import random
import json
from flask import Flask, request, jsonify


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
        return jsonify({"erro": "Cliente não encontrado. Por favor, forneça um CPF válido."}), 400

    return jsonify({"suporte": f"Suporte técnico iniciado para {cliente['nome']} (CPF: {cpf})."}), 200


@app.route('/suporte/faturamento', methods=['POST'])
def suporte_faturamento():
    dados = request.json
    cpf = dados.get('cpf')

    # Confirmação de dados
    cliente = confirmar_dados(cpf)
    if not cliente:
        return jsonify({"erro": "Cliente não encontrado. Por favor, forneça um CPF válido."}), 400

    boleto = consultar_boleto(cpf)
    return jsonify({
        "suporte": f"Emissão da segunda via de fatura iniciada para {cliente['nome']} (CPF: {cpf}).",
        "boleto": boleto
    }), 200


@app.route('/suporte/instalacao', methods=['POST'])
def suporte_instalacao():
    dados = request.json
    cpf = dados.get('cpf')

    # Confirmação de dados
    cliente = confirmar_dados(cpf)
    if not cliente:
        return jsonify({"erro": "Cliente não encontrado. Por favor, forneça um CPF válido."}), 400

    return jsonify({"suporte": f"Agendamento de instalação feito para {cliente['nome']} (CPF: {cpf})."}), 200


@app.route('/teste/velocidade', methods=['POST'])
def teste_velocidade():
    dados = request.json
    cpf = dados.get('cpf')

    # Confirmação de dados
    cliente = confirmar_dados(cpf)
    if not cliente:
        return jsonify({"erro": "Cliente não encontrado. Por favor, forneça um CPF válido."}), 400

    velocidade = realizar_teste_velocidade()
    return jsonify({
        "suporte": f"Teste de velocidade realizado para {cliente['nome']} (CPF: {cpf}).",
        "velocidade": velocidade
    }), 200


if __name__ == '__main__':
    app.run(debug=True)

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
        return jsonify({"erro": "Cliente não encontrado. Por favor, forneça um CPF válido."}), 400

    return jsonify({"suporte": f"Suporte técnico iniciado para {cliente['nome']} (CPF: {cpf})."}), 200


@app.route('/suporte/faturamento', methods=['POST'])
def suporte_faturamento():
    dados = request.json
    cpf = dados.get('cpf')

    # Confirmação de dados
    cliente = confirmar_dados(cpf)
    if not cliente:
        return jsonify({"erro": "Cliente não encontrado. Por favor, forneça um CPF válido."}), 400

    boleto = consultar_boleto(cpf)
    return jsonify({
        "suporte": f"Emissão da segunda via de fatura iniciada para {cliente['nome']} (CPF: {cpf}).",
        "boleto": boleto
    }), 200


@app.route('/suporte/instalacao', methods=['POST'])
def suporte_instalacao():
    dados = request.json
    cpf = dados.get('cpf')

    # Confirmação de dados
    cliente = confirmar_dados(cpf)
    if not cliente:
        return jsonify({"erro": "Cliente não encontrado. Por favor, forneça um CPF válido."}), 400

    return jsonify({"suporte": f"Agendamento de instalação feito para {cliente['nome']} (CPF: {cpf})."}), 200


@app.route('/teste/velocidade', methods=['POST'])
def teste_velocidade():
    dados = request.json
    cpf = dados.get('cpf')

    # Confirmação de dados
    cliente = confirmar_dados(cpf)
    if not cliente:
        return jsonify({"erro": "Cliente não encontrado. Por favor, forneça um CPF válido."}), 400

    velocidade = realizar_teste_velocidade()
    return jsonify({
        "suporte": f"Teste de velocidade realizado para {cliente['nome']} (CPF: {cpf}).",
        "velocidade": velocidade
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
