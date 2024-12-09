import sqlite3 #importação da tabela mysqlLite
con = sqlite3.connect("dados.db") # isso realiza a conecção com o banco de dados, ou criar um arquivos se não existir um.
executar_comandos_sqlite = con.cursor() #isso executa comandos sqlite

executar_comandos_sqlite.execute('''
CREATE TABLE IF NOT EXISTS cliente(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente TEXT NOT NULL,
    cpf INTEGER
)
''')
