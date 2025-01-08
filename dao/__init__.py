import psycopg2

def conectardb():
    con = psycopg2.connect(
        host='localhost',
        database='consultaifpb',
        user='postgres',
        password='12345'
    )
    return con

conectardb()


def inserirusuario(nome, email, senha):
 conexao = conectardb()
 cur = conexao.cursor()
 exito = False

 try:
  sql = f"INSERT INTO usuario (nome, email, senha) VALUES ('{nome}', '{email}','{senha}')"
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
    cur.execute(f”SELECT
    email, nome
    FROM
    usuario
    WHERE
    email = ‘{email}’ AND
    senha = ‘{senha}’”)
    recset = cur.fetchall()
    cur.close()
    conexao.close()
    return recset


def inseriragendamento(nome, telefone, email, dia_consulta, nome_pet, especie,
                       motivo):
    conexao = conectardb()
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"INSERT INTO agendamento (nome, telefone, emai, nome_pet, especie,
motivo) VALUES('{nome}', '{telefone}', '{email}', '{dia_consulta}', '{nome_pet}',
'{motivo')"
cur.execute(sql)
except psycopg2.Error:
conexao.rollback()
exito = False
else:
conexao.commit()
exito = True
conexao.close()
return exito


def get_usuario_por_nome(self, nome_usuario):
    try:
        cursor = self.connection.cursor(dictionary=True)
    query = “SELECT * FROM
    usuarios
    WHERE
    nome_usuario = %s”
    cursor.execute(query, (nome_usuario,))
    resultado = cursor.fetchone()  # Obtém um único registro
    cursor.close()
    return resultado
    except mysql.connector.Error as err:
    print(f”Erro
    ao
    acessar
    o
    banco
    de
    dados: {err}”)
    return None