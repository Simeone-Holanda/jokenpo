from .. import db


class Jogada(db.Model):
    __tablename__ = 'jogadas'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)

    simbolo = db.Column(db.String(30), nullable=False)
    jogador_id = db.Column(db.Integer, db.ForeignKey('jogadores.id'))

    def __repr__(self):
        return self.simbolo
