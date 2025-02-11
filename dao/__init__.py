import psycopg2

def conectardb():
    con = psycopg2.connect(
        host='localhost',
        database='hospif',
        user='postgres',
        password='12345'
    )
    return con

def inserirusuario(nome, email, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO usuario (nome, email, senha) VALUES ('{nome}', '{email}', '{senha}')"
        cur.execute(sql)
    except psycopg2.Error:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito



def verificarlogin(email, senha):
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute(f"SELECT email, nome FROM usuario WHERE email = '{email}' AND senha = '{senha}'")
    recset = cur.fetchall()
    cur.close()
    conexao.close()

    return recset


def inserir_agendamento(nome, telefone, email, dia_consulta, nome_pet, especie, motivo, conexao):
    exito = False
    try:
        sql = """
            INSERT INTO agendamento (nome, telefone, email, nome_pet, especie, motivo) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur = conexao.cursor()
        cur.execute(sql, (nome, telefone, email, nome_pet, especie, motivo))
    except psycopg2.Error as err:
        print(f"Erro ao executar a consulta: {err}")
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True
    finally:
        cur.close()
        conexao.close()
    return exito


















