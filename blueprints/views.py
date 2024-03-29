from flask import request, render_template, Blueprint
from blueprints.swich_calculo import *
from blueprints.mudar_venc import *
from blueprints.calculos import CalculoDesc
from blueprints.cancelar_client import Calculo_cancelamento
from blueprints.negociacao import Calculo_negociacao
import pandas as pd

Telas = Blueprint('Telas', __name__)

@Telas.route("/", methods=['POST','GET'])
def Home():
    return render_template('index.html')

@Telas.route("/homepage", methods=['POST', 'GET'])
def homepage():
    resultado = S_venc(pVen=request.form.get('vencimento'), pAtual=request.form.get('planoAtual'), pNovo=request.form.get('planoNovo'), checkA=request.form.get('cidadeAnanindeua'), Data_Solicitacao = request.form.get("dataSolicitacao"))

    return render_template("homepage.html", resultado=resultado)
@Telas.route("/homepage2", methods=['POST','GET'])

def homepage2():
    resultadoVencimento = MudarVen(vAtual=request.form.get('vencimentoAtual'), vNovo=request.form.get('vencimentoNovo'), vPlano=request.form.get('planoCliente'), checkA=request.form.get('cidadeAnanindeua'), Data_Solicitacao = request.form.get("dataSolicitacao"))

    return  render_template("homepage2.html", resultadoVencimento = resultadoVencimento)
@Telas.route("/homepage3", methods=['POST','GET'])
def homepage3():
    resultadoDesc =  CalculoDesc(Plano = request.form.get('Plano'),D = request.form.get('D'), M = request.form.get('M'), Data_Solicitacao = request.form.get("dataSolicitacao"))
    return render_template("homepage3.html", resultadoDesc = resultadoDesc)

@Telas.route("/homepage4", methods=['POST','GET'])
def homepage4():
    resultado_cancelamento = Calculo_cancelamento(pAtual = request.form.get("Plano_cancelamento"), pVen = request.form.get("vencimento_cancelamento"), Data_Solicitacao = request.form.get("dataSolicitacao"),data_ati = request.form.get("data_ati"),multa=request.form.get("multa"))
    return render_template("homepage4.html", resultado_cancelamento=resultado_cancelamento)

@Telas.route("/homepage5", methods=['POST','GET'])
def homepage5():
    campos_adicionais = []
    for key, value in request.form.items():
        if key.startswith('data') or key.startswith('valor') or key.startswith('dias') or key.startswith('multa') or key.startswith('juros') or key.startswith('cobrar'):
            campos_adicionais.append(value)

    try:
        r = Calculo_negociacao(campos_adicionais)
        return render_template("homepage5.html", resultados=r)
    except ValueError:

        return render_template("homepage5.html", resultados= "!!!", error="Error no envio do formulario (Vazio)" )








