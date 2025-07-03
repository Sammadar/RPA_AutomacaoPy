#No que consta a automação:
# abrir um arquivo txt com varios cnpj´s
# consultar cada cnpj na API do invertexto
# salvar o resultado da consulta no bancco de MYSQL
# só devem ser consultados os novos dados inseridos
#tupla - lista imutável

import re
import requests
from pymsgbox import password

from tokenCNPJ import API_TOKEN
import pymysql

def conectar_banco():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        port=3306,
        database='cnpjs'
    )
    conn_cursor = conn.cursor()
    return conn,conn_cursor

def consultar_cadastro(cnpj_procurado):
    #verificar se o CNPJ já está no banco
    conexao_consulta, cursor_consulta = conectar_banco()
    query = '''
    SELECT COUNT(*) FROM cnpjs
    WHERE cnpj = %s;
    '''
    cursor_consulta.execute(query, (cnpj_procurado,))
    resultado = int(cursor_consulta.fetchone()[0]) > 0
    cursor_consulta.close()
    conexao_consulta.close()
    return resultado


cnpjs = open('cnpj.txt', 'r').read().splitlines()
for cnpj in cnpjs:
    # remover caracteres não numericos do CNPJ
    cnpj_corrigido = re.sub(r'\D','', cnpj)
    if consultar_cadastro(cnpj_corrigido):
        print(f'cnpj {cnpj} já cadastrado')
        continue

    #consultar API
    url = f'https://api.invertexto.com/v1/cnpj/{cnpj_corrigido}?token={API_TOKEN}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        razao_social, data_inicio = dados['razao_social'],dados['data_inicio']
        conexao, cursor = conectar_banco()

        # instrução SQL para inserir no banco : %s serve como máscara para ser substituido no comando cursor.execute
        query = 'INSERT INTO cnpjs(cnpj, razaoSocial, dataInicio) VALUES (%s,%s,%s);'

        valores = (cnpj_corrigido, razao_social, data_inicio)
        cursor.execute(query, valores) #executar a instrução SQL
        conexao.commit()

        #fechar conexão e cursor
        cursor.close()
        conexao.close()
        continue
    if response.status_code == 422:
        print(f'CNPJ {cnpj} não foi encontrado')
        continue
