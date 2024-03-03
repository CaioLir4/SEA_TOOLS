
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import calendar

from blueprints.planos import *

def Calculo_negociacao1(valorBoleto, Data_Solicitacao ):
    data_hoje = datetime.strptime(Data_Solicitacao, "%Y-%m-%d").date() if (Data_Solicitacao != "") and (Data_Solicitacao != None) else date.today()
    Data_SolicitacaoBr = data_hoje.strftime("%d-%m-%Y")
    
    if valorBoleto == None: 
        return "resultado"
    
    else:
    
        data_calc = date.today() - data_hoje
        
        ProxAtual = (data_hoje.month % 12) + 1
    
        multa  = valorBoleto * 0.02 
    
        juros = valorBoleto * 0.00033 * data_calc.days
    
        valor_total = valorBoleto + multa + juros
    
        r = f"Data Simulada:{Data_SolicitacaoBr}\nValor Boleto:{valorBoleto}\nResultado:{valor_total:.2f} "
        return r 

import csv
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import calendar
from blueprints.planos import *

def Calculo_negociacao(pAtual, Data_Solicitacao):
    data_hoje = datetime.strptime(Data_Solicitacao, "%Y-%m-%d").date() if (Data_Solicitacao != "") and (Data_Solicitacao != None) else date.today()
    Data_SolicitacaoBr = data_hoje.strftime("%d-%m-%Y")
    
    
    plano_atual = (globals()[f"plan{pAtual}"]())
    
    data_calc = date.today() - data_hoje
        
    ProxAtual = (data_hoje.month % 12) + 1
    
    multa  = plano_atual * 0.02 
    
    juros = plano_atual * 0.00033 * data_calc.days
    
    valor_total = plano_atual + multa + juros
    
    r = f"Data Simulada:{Data_SolicitacaoBr}\nPlano Atual:{plano_atual}\nResultado:{valor_total:.2f} "

    return r