from .. import ma
from ..models.jogador import Jogador
from marshmallow import fields, validates, ValidationError


class JogadorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Jogador
        fields = ("id", "name", )  # jogadas
        include_fk = True
        include_relationships = True

    name = fields.Str(required=True)
