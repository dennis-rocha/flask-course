from db import db

class AgendamentoModels(db.Model):
    __tablename__ = "agendamento"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), unique=False, nullable=False)
    clientes = db.relationship("ClienteModels", back_populates="agendamentos")