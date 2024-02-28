from blueprints.calculos import *

def S_venc(pVen, pAtual, pNovo, checkA, Data_Solicitacao):
    if checkA:
        return CalculoA(pAtual, pNovo, pVen, Data_Solicitacao)  # VENCIMENTO DE ANANINDEUA
    elif pVen in ["5", "10"]:
        return Calcularven1(pAtual, pNovo, pVen, Data_Solicitacao)  # VENCIMENTO 5 OU 10
    elif pVen in ["15", "20"]:
        return Calcularven2(pAtual, pNovo, pVen, Data_Solicitacao)  # VENCIMENTO 15 OU 20
    elif pVen in ["25", "30"]:
        return Calcularven3(pAtual, pNovo, pVen, Data_Solicitacao)  # VENCIMENTO 25 OU 30
