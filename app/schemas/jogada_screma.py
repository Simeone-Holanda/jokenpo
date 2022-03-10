from .. import ma
from ..models.jogada import Jogada
from marshmallow import fields, validates, ValidationError


class JogadaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Jogada
        fields = ("id","simbolo", "jogador_id")
        include_fk = True
        load_instance = True

    simbolo = fields.Str(required=True)

    @validates('simbolo')
    def validate_simbolo(self, value):
        if value not in ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']:
            raise ValidationError(
                "Simbolo não existe! Verifiquei os disponiveis -> [pedra, papel, tesoura, largato, spock]")
