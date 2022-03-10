from flask import jsonify
from flask import Blueprint

# from application.models import Jogador

views = Blueprint('views', __name__)

lista_rodadas = []


@views.route('/', methods=['GET'])
def get_test():
    return jsonify({'status': '200'})


@views.route('/<string:jogador>/<string:jogada>', methods=['GET'])
def send_play(jogador: str, jogada: str):
    rodada = {
        'jogador': jogador,
        'jogada': jogada
    }
    lista_rodadas.append(rodada)
    return jsonify({'status': '200'})


@views.route('/jogar', methods=['GET'])
def get_result_play():
    lista_jogadas = [rodada['jogada'] for rodada in lista_rodadas]
    result = get_winer(lista_jogadas[0], lista_jogadas[1])
    return jsonify(result)


def get_winer(jogada1, jogada2):
    if jogada1 == jogada2:
        delete_jogador(jogada1)
        delete_jogador(jogada2)
        return {'resultado': 'Empate'}
    elif jogada1 == 'tesoura':
        if jogada2 == 'pedra':
            delete_jogador(jogada1)
            delete_jogador(jogada2)
            return {'resultado': 'Jogador 2 Venceu'}
        else:
            delete_jogador(jogada1)
            delete_jogador(jogada2)
            return {'resultado': 'Jogador 1 Venceu'}
    elif jogada1 == 'pedra':
        if jogada2 == 'tesoura':
            delete_jogador(jogada1)
            delete_jogador(jogada2)
            return {'resultado': 'Jogador 1 Venceu'}
        else:
            delete_jogador(jogada1)
            delete_jogador(jogada2)
            return {'resultado': 'Jogador 2 Venceu'}
    elif jogada1 == 'papel':
        if jogada2 == 'tesoura':
            delete_jogador(jogada1)
            delete_jogador(jogada2)
            return {'resultado': 'Jogador 2 Venceu'}
        else:
            delete_jogador(jogada1)
            delete_jogador(jogada2)
            return {'resultado': 'Jogador 1 Venceu'}


def delete_jogador(jogador):
    for rodada in lista_rodadas:
        if rodada['jogador'] == jogador:
            lista_rodadas.remove(rodada)
