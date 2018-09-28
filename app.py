from flask import Flask, jsonify, make_response, request
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

@app.route('/usuarios/<string:email>')
def get_usuarios(email=None):
    query = {'email' : email} if email else {}
    db = client['flask-app']
    usuarios = [remover_id(u) for u in db.usuarios.find(query)]
    if usuarios:
        return jsonify(usuarios)
    else:
        return make_response(jsonify({'message' : 'usuario nao encontrado.'}), 404)

@app.route('/usuarios', methods=['POST'])
def post_usuarios():
    data = request.get_json()
    for k in ['nome', 'email', 'profissao']:
        if k not in data:
            return make_response(jsonify({'message' : 'Propriedade {0} obrigatória.'.format(k)}), 400)

    db = client['flask-app']
    db.usuarios.insert(data)
    return make_response(jsonify({'message' : 'usuario cadastrado com sucesso.'}), 201)

@app.route('/usuarios/<string:email>', methods=['DELETE'])
def del_usuarios(email):
    db = client['flask-app']
    db.usuarios.remove({'email' : email})
    return make_response(jsonify({'message' : 'usuario removido.'}), 200)

@app.route('/usuarios/<string:email>', methods=['PUT'])
def put_usuarios(email):
    data = request.get_json()
    db = client['flask-app']
    db.usuarios.update({'email' : email}, {'$set' : data})
    return make_response(jsonify({'message' : 'usuario atualizado com sucesso.'}), 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=88, debug=True)

# datetime - 
# return jsonify({'hoje': datetime.now()})
