from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'lucas'
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('warzone', 'tiro', 'PC')
jogo2 = Jogo('rainbow six', 'tiro', 'PC')
jogo3 = Jogo('need for speed', 'corrida', 'PC')
lista = [jogo1, jogo2, jogo3]

class User:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

usuario = User('Lucas', 321)
usuario1 = User('João', 321)
usuario2 = User('Maria', 321)

usuarios = {usuario.nome: usuario, usuario1.nome: usuario1, usuario2.nome: usuario2}

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/logout')
def logout():
    session['user'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))

@app.route('/autenticar', methods = ['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario_busca = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario_busca.senha:
            session['user'] = usuario_busca.nome
            flash(usuario_busca.nome + ' usuario logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuario não logado!')
        return redirect(url_for('login'))

@app.route('/novo')
def novo():
    if 'user' not in session or session['user'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Adicionar novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return redirect(url_for('index'))

app.run(debug=True)