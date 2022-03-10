

def get_win(jogadas: list):
    """ Método responsável por analisar todas as rodadas e obter o vencedor. 

    param:
        jogadas: Lista de todas as jogadas realizadas na rodada.

    return: 
        O vencedor da rodada caso não tenha sido empate
    """

    regras_jogo = {
        'pedra': {
            'ganha': ['tesoura', 'lagarto'],
            'perde': ['papel', 'spock']
        },
        'lagarto': {
            'ganha': ['spock', 'papel'],
            'perde': ['pedra', 'tesoura']
        },
        'spock': {
            'ganha': ['tesoura', 'pedra'],
            'perde': ['papel', 'lagarto']
        },
        'tesoura': {
            'ganha': ['lagarto', 'papel'],
            'perde': ['spock', 'pedra']
        },
        'papel': {
            'ganha': ['spock', 'pedra'],
            'perde': ['lagarto', 'tesoura']
        },
    }

    jogadas_atualizadas = []

    for jogada in jogadas:
        regras_simbolo = regras_jogo[jogada['simbolo']]
        jogadas_oponentes = jogadas.copy()
        jogadas_oponentes.remove(jogada)
        ponto = 0
        for jogada_oponente in jogadas_oponentes:
            if jogada_oponente['simbolo'] in regras_simbolo['ganha']:
                ponto += 1
            elif jogada_oponente['simbolo'] in regras_simbolo['perde']:
                ponto -= 1
            else:
                print(f'{jogada_oponente} empatou com {jogada}')
        jogada['pontos'] = ponto
        jogadas_atualizadas.append(jogada)

    vencedor = check_points(jogadas_atualizadas)
    return vencedor


def check_points(jogadas_rodada: list):
    """ Método responsável por analisar qual jogada teve mais pontos. 

    param:
        jogadas_rodada: Lista de todas as jogadas realizadas na rodada.

        [NOTE]: Essas jogadas já vem com sua pontuação. 

    return: 
        um dicionaio com os dados do jogador que teve mais pontos na rodada
    """

    max_pontos_rodada = jogadas_rodada[0]
    for jogada in jogadas_rodada:
        if jogada['pontos'] >= max_pontos_rodada['pontos']:
            max_pontos_rodada = jogada

    pontos_rodada = [jogada["pontos"] for jogada in jogadas_rodada]
    
    if pontos_rodada.count(max_pontos_rodada['pontos']) > 1:
        return "Sem resultados exatos, rodada empatada. "

    return max_pontos_rodada


def check_player_played(jogadas_rodada: list, jogador) -> bool:
    """ Verificar se o usuário ja realizou alguma jogada na rodada. 
    param:
        jogadas_rodada: Lista de todas as jogadas realizadas na rodada.

    return: 
        True caso o usuário ja tenha jogado alguma vez nessa rodada ou False 
        caso não tenha.
    """
    for jogada_rodada in jogadas_rodada:
        if jogada_rodada['jogador'] == jogador.name:
            return True
    return False
