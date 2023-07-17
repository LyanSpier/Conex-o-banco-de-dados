import mysql.connector
def conectar():
    host = 'localhost'
    usuario = 'root'
    senha = 'admin'
    banco_de_dados = 'laylasupermercados'
    
    conexao = mysql.connector.connect(
        host = host,
        user = usuario,
        password = senha,
        database = banco_de_dados
    )
    
    return conexao

def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF DO NOT EXIST aluno(       
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            data_nacsimento DATE,
            cidade_natal VARCHAR(255),
            bairoo VARCHAR(255)
        ) 
    ''')
    conexao.commit()
    def cadastrar_aluno(conexao,nome,data_nascimento,cidade_natal,bairro):
        cursor = conexao.cursor()
        
        inserir_query = '''
        INSERT INTO aluno(nome,data_nascimento,cidade_natal,bairro)
        VALUES(%s,%s,%s,%s)
        
        '''
        valores = (nome,data_nascimento,cidade_natal,bairro)
        cursor.execute(inserir_query,valores)
        conexao.commit()