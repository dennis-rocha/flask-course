from db import db

class ClienteModels(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)    
    endereco_logradouro = db.Column(db.String, nullable=False)
    endereco_numero = db.Column(db.String, nullable=False)
    endereco_complemento = db.Column(db.String, nullable=False)
    endereco_municipio = db.Column(db.String, nullable=False)
    endereco_bairro = db.Column(db.String, nullable=False)
    endereco_uf = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String, nullable=False)