#importando o flask
import psycopg2
from flask import *
import dao

app = Flask(__name__)
app.secret_key = 'X8f4Z1p9LdWvHo3T'

@app.route('/')
def pageprincipal():
    return render_template('index.html')


@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    if dao.inserirusuario(nome, email, senha):
        msg = 'Usuário cadastrado com sucesso'
    else:
        msg = 'Problemas ao cadastrar o usuário'
    return render_template('index.html', mensagem=msg)


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    resultado = dao.verificarlogin(email, senha)

    if resultado and len(resultado) > 0:
        session['login'] = resultado[0][1]
        return render_template('logon.html', user=resultado[0][1])
    else:
        msg = 'Senha ou login incorretos'
        return render_template('index.html', msglogin=msg)


@app.route('/agendamento', methods=['POST'])
def agendamento():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')  # Corrigido uso de aspas simples
    email = request.form.get('email')
    dia_consulta = request.form.get('dia-consulta')
    nome_pet = request.form.get('nome-pet')
    especie = request.form.get('especie')
    motivo = request.form.get('motivo')

    if dao.inseriragendamento(nome, telefone, email, dia_consulta, nome_pet, especie, motivo):
        msg = 'Agendamento realizado com sucesso'
    else:
        msg = 'Problemas ao realizar agendamento'
    return render_template('logon.html', mensagem=msg)


@app.route('/visualizar_informacoes')
def visualizar_informacoes():
    informacoes = dao.get_informacoes()
    return render_template('informacoes.html', informacoes=informacoes)


def insert_comentario(login, comentario, conexao):
    cur = conexao.cursor()
    exito = False
    try:
        sql = f"UPDATE usuario SET comentario = '{comentario}' WHERE login = '{login}'"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True
    finally:
        cur.close()
        conexao.close()
    return exito


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == '_main_':
    app.run(debug=True)