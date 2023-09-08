from marshmallow import fields, Schema

class PlainClienteSchema (Schema):
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

class PlainAgendamentoSchema (Schema):
    id = fields.Int(dump_only=True)
    data = fields.Date(required=True)

class ClienteSchema(PlainClienteSchema):
    agendamento = fields.List(fields.Nested(lambda: AgendamentoSchema()), dump_only=True)

class AgendamentoSchema(PlainAgendamentoSchema):
    cliente_id = fields.Int(required=True, load_only=True)
    clientes = fields.Nested(lambda: ClienteSchema(), dump_only=True)
    
