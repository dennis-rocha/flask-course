from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from schemas import AgendamentoSchema
from models import AgendamentoModels

blp = Blueprint("Agendamento", __name__, description="Operações para obter dados dos agendamentos")


@blp.route("/agendamento")
class Agendamento(MethodView):

    @blp.response(200,AgendamentoSchema(many=True))
    def get(self):
        return AgendamentoModels.query.all()
    
    @blp.arguments(AgendamentoSchema)
    @blp.response(200,AgendamentoSchema)
    def post(self,data):
        # FIXME Criar função para validar a data de entrada. Para agendmento somente data futura
        #from pdb import set_trace;set_trace()
        item = AgendamentoModels(**data)
        try:
            db.session.add(item)
            db.session.commit()
        
        except Exception as err:
            print(err)
            abort(500, "Ocorreu um erro ao salvar os dados")

        return item