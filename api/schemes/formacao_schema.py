from api import ma
from ..models import formacao_model
from marshmallow import fields
from ..schemes import curso_schema, professor_schema


class FormacaoSchema(ma.SQLAlchemyAutoSchema):
    professores = ma.Nested(professor_schema.ProfessorSchema, many=True, only=('id', 'nome'))

    class Meta:
        model = formacao_model.Formacao
        load_instance = True
        fields = ("id", "nome", "descricao", "cursos", "professores", "_links")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    cursos = fields.List(fields.Nested("CursoSchema", only=('id', 'nome')))

    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor('cursodetail', values={'id': '<id>'}),
            "put": ma.URLFor('cursodetail', values={'id': '<id>'}),
            "delete": ma.URLFor('cursodetail', values={'id': '<id>'})
        }
    )
