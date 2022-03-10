from flask import jsonify, Blueprint, request
from marshmallow import ValidationError
from .. import db
from ..models.jogador import Jogador
from ..models.jogada import Jogada
from ..services.jokenpo import get_win, check_player_played
from ..schemas.jogada_screma import JogadaSchema

views_round = Blueprint('views_round', __name__)

jogadas_rodada = []


@views_round.route('/', methods=['GET'])
def home():
    """ Método apenas para obter o status da api. """
    return jsonify({'status': '200', 'message': 'API working'})


@views_round.route('/jogada/', methods=['POST'])
def send_play():
    """
        Método usado para realizar/cadastrar a jogada de um jogador.
    """
    play_data = request.get_json()
    name_jogador = play_data['jogador']
    jogador = Jogador.query.filter_by(name=name_jogador).first()
    if not jogador:
        return jsonify({'response': f'Error {name_jogador} player not exist.'})

    serializer_play = play_data.copy()
    serializer_play['jogador_id'] = jogador.id
    del serializer_play['jogador']

    try:
        jogada_schema = JogadaSchema()
        new_play = jogada_schema.load(serializer_play)
        db.session.add(new_play)
        db.session.commit()
    except ValidationError as ex:
        return jsonify({'status': 400, 'message': ex.messages})

    if len(jogadas_rodada) > 0:
        if check_player_played(jogadas_rodada, jogador):
            return jsonify({'response': f'Error {jogador} cannot play twice in the round.'})

    jogadas_rodada.append(play_data)
    return jsonify({'status': '201', 'data': play_data})


@views_round.route('/finalizar-rodada/', methods=['GET'])
def result_play():
    """ Verifica quem foi o vencedor da rodada. """

    if len(jogadas_rodada) >= 2:
        result = get_win(jogadas_rodada)
        jogadas_rodada.clear()
        return jsonify({'status': '200', 'vencedor': result})
    else:
        return jsonify({'status': '200', 'message': 'Necessário que sejam realizadas ao menos duas jogadas. '})


@views_round.route('/jogadas/<string:nome_jogador>', methods=['GET'])
def show_plays(nome_jogador):
    jogador = Jogador.query.filter_by(name=nome_jogador).first()
    if not jogador:
        return jsonify({'response': f'Error {nome_jogador} player not exist.'})
    jogada_schema = JogadaSchema(many=True)
    jogadas = jogada_schema.dump(jogador.jogadas)
    return jsonify({'status': '200', 'jogadas': jogadas})


@views_round.route('/jogadas/delete/<jogada_id>', methods=['DELETE'])
def remove_play(jogada_id):
    jogador = Jogada.query.filter_by(id=jogada_id)
    if not jogador:
        return jsonify({'response': f'Error player not exist.'})
    jogador.delete()
    db.session.commit()
    return jsonify({'message': 'No content'})
