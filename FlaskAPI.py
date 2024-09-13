from flask import Flask, jsonify
import user

app = Flask(__name__)

#Rota de exemplo

@app.route('/nome', methods=['GET'] )

def getNome():
    dados = user.Alunos
    dados2 = user.Professores
    return jsonify(dados["alunos"],dados2["profs"])

if __name__ == '__main__':
    app.run(debug=True)