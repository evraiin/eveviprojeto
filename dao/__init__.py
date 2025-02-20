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



def inserir_agendamento(nome, diaconsulta, motivo, email):
    print(nome, diaconsulta, motivo, email)
    try:
        conexao = conectardb()
        cur = conexao.cursor()
        sql = f"INSERT INTO agendamentos (nome, diaconsulta, motivo, email) VALUES ('{nome}', '{diaconsulta}', '{motivo}', '{email}')"
        cur.execute(sql)
    except Exception as e:
        print(e)
        return False
    else:
        conexao.commit()
        conexao.close()
        return True



















