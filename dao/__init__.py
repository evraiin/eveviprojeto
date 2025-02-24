import psycopg2

def conectardb():
    con = psycopg2.connect(
        host='dpg-curo7dan91rc73c1q6i0-a.oregon-postgres.render.com',
        database='projetohv',
        user='projetohv_user',
        password='8VxJN4fYGdmE1S0U8UcNz5cY6NJJO3Cj'
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


def listar_user():
    conexao = conectardb()
    cur = conexao.cursor()
    cur.execute("SELECT nome FROM usuario")

    recset = cur.fetchall()
    conexao.close()

    return recset

def inseriranimal(nome, especie, raca, idade, sexo, peso):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO animal (nome, especie, raca, idade, sexo, peso) VALUES ('{nome}', '{especie}', '{raca}', '{idade}', '{sexo}' , '{peso}')"
        cur.execute(sql)
    except psycopg2.Error as e:
        print(e)
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito



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



















