from flask import Flask, jsonify, make_response
from datetime import datetime
from pymongo import MongoClient

client = MongoClient()

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'status': 'Running!'})


def remover_id(u):
    del u['_id']
    return u

# criar rota chamada hoje
# importar modulo datetime e escrever a data de hoje .now()
# na rota hoje, retornar a data dentro de um json no seguinte formato
# {"hoje" : "....................."}

@app.route('/usuarios')
#def usuarios():
#    db = client['flask-app']
#    print(db.usuarios.find_one())
# [] = LISTA do Python

#   cursor = db.usuarios.find()
#   usuarios = []
#   for usuario in cursor: 
#       del usuario['_id']
#       usuarios.append(usuario)
#   return jsonify(usuarios)

# evolucao do codigo acima

#   usuarios = []
#   for usuario in db.usuarios.find():
#       del usuario['_id']
#       usuarios.append(usuario)
#   return jsonify(usuarios)

#evolucao do codigo acima:

def usuarios():
    db = client['flask-app']
    return jsonify([remover_id(u) for u in db.usuarios.find()])

# datetime - 
# return jsonify({'hoje': datetime.now()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
