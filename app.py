from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Usuários fictícios para autenticação (substitua por um banco de dados real)
usuarios = {
    "usuario1@example.com": "senha123",
    "usuario2@example.com": "senha456"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("password")
        # Verifica se o usuário existe e a senha está correta
        if email in usuarios and usuarios[email] == senha:
            return redirect(url_for("home"))  # Redireciona para a tela inicial
        else:
            return render_template("login.html", erro="Usuário ou senha inválidos!")

    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/equipamentos")
def equipamentos():
    return render_template("equipamentos.html")

@app.route("/analise")
def analise():
    return render_template("analise.html")

@app.route("/informativos")
def informativos():
    return render_template("informativos.html")

@app.route('/configuracoes')
def configuracoes():
    return render_template('configuracoes.html')

@app.route('/seguranca')
def seguranca():
    return render_template('seguranca.html')

@app.route("/mapa")
def mapa():
    return render_template("mapa.html")

@app.route("/alertas")
def alertas():
    return render_template("alertas.html")

@app.route("/dashboard/opcoes")
def dashboard_opcoes():
    return render_template("dashboard_opcoes.html")
    
@app.route("/graficos")
def graficos():
    return render_template("graficos.html")

if __name__ == "__main__":
    app.run(debug=True)
