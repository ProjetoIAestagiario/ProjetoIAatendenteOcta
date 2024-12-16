# Importa os módulos necessários para ajustar o caminho do projeto
import sys
import os

# Adiciona o diretório principal do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Agora você pode importar bibliotecas do diretório principal
from bibliotecas.importacoes import *
from function.voz.voz import *
import datetime

def saudacao_cliente():
    hora = datetime.datetime.now().hour
    if 6 <= hora < 12:
        falar("Bom dia! Eu sou Óto, o assistente virtual da ÓctaTelecom.")
        falar("Estou aqui para ajudar você com qualquer dúvida ou suporte relacionado aos nossos serviços de internet. Em que posso ajudar você?")
    elif 12 <= hora < 18:
        falar("Boa tarde! Eu sou Óto, o assistente virtual da ÓctaTelecom.")
        falar("Estou aqui para ajudar você com qualquer dúvida ou suporte relacionado aos nossos serviços de internet. Em que posso ajudar você?")
    else: 
        falar("Boa noite! Eu sou Óto, o assistente virtual da ÓctaTelecom.")
        falar("Estou aqui para ajudar você com qualquer dúvida ou suporte relacionado aos nossos serviços de internet. Em que posso ajudar você?")


#isso mostra a data a tual só que não no formato brasileiro
#from datetime import datetime
#seu eu dizer que avarivel "data_atual" vai receber "date.today()" e imprimir vai mostra a data atual só que no formato internacional(2024-12-10).
#data_atual = date.today()
#para resolver isso, bata eu formatar para o Brasileiro, da sequinte forma:
#crio uma variavel, depois atribuo ela a ela mesma só que passando o seguinte paramento que realizara a formatação separando avariavel do paramento(strftime('%d/%m/%Y')) por um "." dentro do parenteses do strftime(''), passo os seguintes %d/%m/%Y fazendo dessa forma estou a dizer para o "strftime" que quero que ele formata nessas seguintes ordens "'%d/%m/%Y'".
""" data_formatado_br = datetime.now()
data_formatado_br_hora = data_formatado_br.strftime('%d/%m/%Y %H:%M')

print(data_formatado_br_hora)
 """


# O arquivo data.hora está dentro da pasta hora que está dentro da pasta function. Já a pasta biblioteca com o arquivo "importacoes.py" está na no diretoiio principal do projeto
