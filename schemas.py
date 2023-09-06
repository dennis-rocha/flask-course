from marshmallow import fields, Schema

class ClienteSchema (Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    endereco_logradouro = fields.Str(required=True)
    endereco_numero = fields.Str(required=True)
    endereco_complemento = fields.Str(required=True)
    endereco_municipio = fields.Str(required=True)
    endereco_bairro = fields.Str(required=True)
    endereco_uf = fields.Str(required=True)
    telefone = fields.Str(required=True)
    email = fields.Str(required=True)

class AgendamentoSchema (Schema):
    id = fields.Int(dump_only=True)
    data = fields.Date(required=True)
    cliente_id = fields.Int()
    cliente = fields.Nested(ClienteSchema,only=('id','nome'))