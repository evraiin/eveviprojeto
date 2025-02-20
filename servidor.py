from flask import *
import dao

app = Flask(__name__)
app.secret_key = 'X8f4Z1p9LdWvHo3T'

@app.route('/')
def pageprincipal():
    return render_template('inicio.html')

@app.route('/login')
def pagina_login():
    return render_template('login.html')

@app.route('/cadastro')
def pagina_cad():
    return render_template('cadastro.html')



@app.route('/cadastro', methods=['POST'])
def inserirusuario():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    if dao.inserirusuario(nome, email, senha):
        msg = 'Usuário cadastrado com sucesso'
    else:
        msg = 'Problemas ao inserir usuário'
    return render_template('login.html', mensagem=msg)

@app.route('/login', methods={'POST'})
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    resultado = dao.verificarlogin(email, senha)

    if len(resultado) > 0:
        session['login'] = resultado[0]

        return render_template('logon.html', usuario=resultado[0])
    else:
        msg = 'Usuario ou senha incorretos'
        return render_template('login.html',  mensagem=msg)



@app.route('/agendar', methods=['POST','GET'])
def agendar():

    if request.method == 'GET' and 'login' in session:
        return render_template('agendamento.html')

    if 'login' not in session:
        return redirect('/logon')


    nome = request.form.get('nome')
    diaconsulta = request.form.get('diaconsulta')
    motivo = request.form.get('motivo')
    email = session['login']
    print(nome, diaconsulta, motivo,email)

    if dao.inserir_agendamento(nome, diaconsulta, motivo,email):
        msgAgendar = 'Agendamento realizado com sucesso!'
        return redirect('/')
    else:

        msgAgendar = 'Ops! Erro ao realizar agendamento, tente novamente.'
        return render_template('agendamento.html', mensagem=msgAgendar)





@app.route('/cadastre', methods={'POST'})
def mostrar_page_login():
    return render_template('cadastro.html')


@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('pageprincipal'))






if __name__ == '__main__':
    app.run(debug=True)


