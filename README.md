# Este projeto foi feito com:
Python 3.9.7 <br>
Flask 2.0.3

## Como rodar o projeto?

1 - Clone esse repositório. <br>
2 - Crie um ambiente virtual com Python.<br>
3 - Ative o virtualenv(O caminho pode variar dependendo do sistema operacional ou terminal usado).<br>
4 - Instale as dependências.<br>
5 - Rode os comandos de configurações.<br>

<br>

1)
``` git clone https://github.com/Simeone-Holanda/jokenpo``` 

``` cd jokenpo ```

2)
``` python -m venv venv```

3)
``` source venv/bin/activate ``` No Linux

``` . venv/Scripts/activate ``` No Windows(com o git bash)

4)
``` pip install -r requirements.txt ```

5)

``` export FLASK_APP=server.py ```

``` flask db init ```

``` flask db migrate ```

``` flask db upgrade ```

``` flask run ```


## Dicas: 
- Na hora de cadastrar um jogador ou uma jogada lembre-se de enviar os dados formato JSON.

- Para cadastrar um jogador basta colocar o seguinte json abaixo no body da rota /criar-jogador/, método requerido -> [POST]

    {
        "name": "Simeone"
    }

- Para cadastrar uma nova jogada basta colocar o json abaixo no body da rota /jogada/ , método requerido -> [POST]

    obs - O jogador precisa está cadastrado no sistema, caso contrario recebera um erro. <br>
{
    "jogador":"Simeone",
    "simbolo":"spock"
}

- Quando acabar de colocar todas as entradas execute a rota /finalizar-rodada/ para obter o vecendor da rodada, método requerido -> [GET]

### Para mais detalhes acesse os arquivos de rotas e poderá ver as funcionalidades abaixo: 
    - Cadastro de jogador -> /criar-jogador/ [POST]
    - Consulta de jogador por id -> /jogadores/<id> [GET]
    - Consulta de todos os jogadores -> /jogadores/ [GET]
    - Remoção de jogador pelo id -> /jogador/delete/<jogador_id> [DELETE]
    - Realização de jogada -> /jogada/ [POST]
    - Finalização da rodada para obter o vencedor -> /finalizar-rodada/ [GET]
    - Consulta a todas as jogadas de um jogador /jogadas/<string:nome_jogador> [GET]
    - Remoção de uma jogada de um jogador pelo id. -> /jogadas/delete/<jogada_id> [DELETE]




<br>
Feito com muito esforço por Simeone Aquino Holanda, espero que gostem. 
