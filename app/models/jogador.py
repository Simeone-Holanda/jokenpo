from .. import db


class Jogador(db.Model):
    __tablename__ = 'jogadores'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)

    name = db.Column(db.String(30), nullable=False, unique=True)
    jogadas = db.relationship('Jogada', backref='jogador')

    def __repr__(self):
        return self.name
