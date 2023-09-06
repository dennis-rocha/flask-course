from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from schemas import ClienteSchema
from models import ClienteModels

blp = Blueprint("Cliente", __name__, description="Operações para obter dados dos clientes")


@blp.route("/cliente")
class Cliente(MethodView):

    @blp.response(200,ClienteSchema(many=True))
    def get (self):
        return ClienteModels.query.all()
    
    @blp.arguments(ClienteSchema)
    @blp.response(200, ClienteSchema)
    def post(self,data):
        item = ClienteModels(**data)
        
        try:
            db.session.add(item)
            db.session.commit()
        except:
            abort(500, "Ocorreu um erro ao salvar os dados")
        
        return item
    
@blp.route("/cliente/<int:id>")
class ClienteId(MethodView):
    
    @blp.response(200,ClienteSchema)
    def get (self, id):
        item = ClienteModels.query.get_or_404(id)
        return item
    
