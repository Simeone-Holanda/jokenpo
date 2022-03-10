from .. import db
from flask import jsonify, request
from flask import Blueprint
from ..models.jogador import Jogador
from ..schemas.jogador_schema import JogadorSchema

views_player = Blueprint('views_player', __name__)


@views_player.route('/jogadores/', methods=['GET'])
@views_player.route('/jogadores/<id>', methods=['GET'])
def show_player(id=None):
    """ Método responsável por obter um jogador"""

    if id != None:
        jogador = Jogador.query.filter_by(id=id).first()
        jogador_schema = JogadorSchema()
        response = jogador_schema.dump(jogador)
        return jsonify({'status': '200', 'data': response})

    jogador_schema = JogadorSchema(many=True)
    jogadores = Jogador.query.all()
    response = jogador_schema.dump(jogadores)
    return jsonify({'status': '200', 'data': response})


@views_player.route('/criar-jogador/', methods=['POST'])
def register_player():
    """ Método responsável por cadastrar um jogador. """
    data_player = request.get_json()
    jogador = Jogador.query.filter_by(name=data_player['name']).first()
    if not jogador:
        new_player = Jogador(name=data_player['name'])
        db.session.add(new_player)
        db.session.commit()
        jogador_schema = JogadorSchema()
        response = jogador_schema.dump(new_player)
        return jsonify({'status': '201', 'data': response})

    return jsonify({'message': 'Name already registered! Try another!'})


@views_player.route('/jogador/delete/<jogador_id>', methods=['DELETE'])
def remove_player(jogador_id):
    jogador = Jogador.query.filter_by(id=jogador_id)
    if not jogador:
        jsonify({'response': f'Error player not exist.'})
    jogador.delete()
    db.session.commit()
    return jsonify({'message': 'No content'})
