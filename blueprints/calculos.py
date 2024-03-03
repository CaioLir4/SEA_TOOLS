import csv
import os
import pandas as pd

from blueprints.planos import *
from datetime import date, datetime
import calendar

# FUNÇÕES DE CACULO DE PLANO -  AQUI ATÉ O PYTHON DEMORA INTERPRETAR
def Calcularven1(pAtual, pNovo, pVen, Data_Solicitacao):
    data_hoje = datetime.strptime(Data_Solicitacao, "%Y-%m-%d").date() if (Data_Solicitacao != "") and (Data_Solicitacao != None) else date.today()
    Data_SolicitacaoBr = data_hoje.strftime("%d/%m/%Y")

    if data_hoje.day != 1:

        quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)[1]
        FinalConusmo = date(data_hoje.year, data_hoje.month, quantidade_dias)
        FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

        # Se o dia atual não for o primeiro do mês
        Day = data_hoje.day - 1
        DayPlAtual = (globals()[f"plan{pAtual}"]()/30) * Day
        RestanteDayNovo = 31 - data_hoje.day if data_hoje.month != 31 else  30 - data_hoje.day
        DayPlNovo = (globals()[f"plan{pNovo}"]()/30) * (RestanteDayNovo)

        ValorTotal = DayPlAtual + DayPlNovo

        IniConsumo = date(data_hoje.year, data_hoje.month, 1)
        IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")

        Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
        AteBr = Ate.strftime("%d/%m/%Y")

        # Criando uma string formatada com os resultados dos cálculos
        r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{Data_SolicitacaoBr} -- {FinalConusmoBr} são {RestanteDayNovo} são totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f} "
    else:
        quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)[1]
        FinalConusmo = date(data_hoje.year, data_hoje.month, quantidade_dias)
        FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

        # Se o dia atual não for o primeiro do mês
        Day = data_hoje.day - 1
        DayPlAtual = (globals()[f"plan{pAtual}"]() / 30) * Day
        RestanteDayNovo = quantidade_dias if quantidade_dias != 31 else 30
        DayPlNovo = (globals()[f"plan{pNovo}"]() / 30) * RestanteDayNovo

        ValorTotal = DayPlAtual + DayPlNovo

        r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n\n{Data_SolicitacaoBr} -- {FinalConusmoBr} são {RestanteDayNovo} são totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f} "

    return r
def Calcularven2(pAtual, pNovo, pVen, Data_Solicitacao):
    data_hoje = datetime.strptime(Data_Solicitacao, "%Y-%m-%d").date() if (Data_Solicitacao != "") and (Data_Solicitacao != None) else date.today()
    Data_SolicitacaoBr = data_hoje.strftime("%d/%m/%Y")

    # Verifica se não é o primeiro dia do mês
    if data_hoje.day != 1:
        # Verifica se não é o primeiro mês do ano
        if data_hoje.month != 1:
            # Calcula para o caso em que a data atual é até o dia 10
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= 10:
                Day = data_hoje.day + 19
                DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 31 - (data_hoje.day + 20)
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month - 1, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}".replace(".",",")

                return r
            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
            # Calcula para o caso em que a data atual é após o dia 10
            else:
                Day = data_hoje.day - 10
                DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 30 - (data_hoje.day - 10)
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}".replace(".",",")

                return r
        # Se for o primeiro mês do ano
        else:
            # Calcula para o caso em que a data atual é até o dia 10
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= 10:
                Day = data_hoje.day + 19
                DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 31 - (data_hoje.day + 20)
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, 12, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}: \nVencimento: {pVen}\n \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}".replace(".",",")

                return r
            # Calcula para o caso em que a data atual é após o dia 10
            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
            else:
                Day = data_hoje.day - 10
                DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 30 - (data_hoje.day - 10)
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year,data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}".replace(".",",")

                return r
    # Se for o primeiro dia do mês
    else:
        # Verifica se não é o primeiro mês do ano
        if data_hoje.month != 1:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            Day = data_hoje.day + 19
            DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
            RestanteDayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = RestanteDayNovo * (globals()[f"plan{pAtual}"]()/30)

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(data_hoje.year, data_hoje.month - 1, 11)
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(data_hoje.year,data_hoje.month, data_hoje.day)
            AteBr = Ate.strftime("%d/%m/%Y")

            FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{Data_SolicitacaoBr} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}".replace(".",",")
#
            return r
        # Se for o primeiro mês do ano
        else:
            Day = data_hoje.day + 19
            DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
            RestanteDayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(data_hoje.year, 12, 11)
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(data_hoje.year, data_hoje.month, data_hoje.day)
            AteBr = Ate.strftime("%d/%m/%Y")

            FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}".replace(".",",")

            return r
def Calcularven3(pAtual, pNovo, pVen, Data_Solicitacao):
    data_hoje = datetime.strptime(Data_Solicitacao, "%Y-%m-%d").date() if (Data_Solicitacao != "") and (Data_Solicitacao != None) else date.today()
    Data_SolicitacaoBr = data_hoje.strftime("%d/%m/%Y")

    DadosVen = [
        (11, 10, 19, 20) if pVen == "15"
        else (11, 10, 19, 20) if pVen == "20"
        else (21, 20, 9, 10) if pVen == "25"
        else (21, 20, 9, 10) if pVen == "30"
        else None]

    if data_hoje.day != 1:
        if data_hoje.month != 1:
            if data_hoje.day <= DadosVen[0][1]:
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 30 - (data_hoje.day + DadosVen[0][2])
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month - 1, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}  ".replace(".",",")

                return r
            else:
                Day = data_hoje.day - DadosVen[0][1]
                DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 30 - (data_hoje.day - DadosVen[0][1])
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f} ".replace(".",",")

                return r
        else:
            if data_hoje.day <= DadosVen[0][1]:
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 30 - (data_hoje.day + DadosVen[0][2])
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, 12, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}  ".replace(".",",")

                return r
            else:
                Day = data_hoje.day - DadosVen[0][1]
                DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 30 - (data_hoje.day - DadosVen[0][1])
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}".replace(".",",")

                return r
    else:
        if data_hoje.month != 1:
            if data_hoje.day <= DadosVen[0][1]:
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual =  Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 30 - (data_hoje.day + DadosVen[0][2])
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month - 1, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}  ".replace(".",",")

                return r
            else:
                Day = data_hoje.day - DadosVen[0][2]
                DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 30 - (data_hoje.day - DadosVen[0][2])
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month - 1, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}  ".replace(".",",")

                return r
        else:
            Day = data_hoje.day + DadosVen[0][2]
            DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
            RestanteDayNovo = 30 - (data_hoje.day + DadosVen[0][2])
            DayPlNovo =  RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(data_hoje.year, 12, DadosVen[0][0])
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(data_hoje.year, data_hoje.month, data_hoje.day)
            AteBr = Ate.strftime("%d/%m/%Y")

            FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}  ".replace(".",",")

            return r

def CalculoDesc(Plano, D, M, Data_Solicitacao):
    data_hoje = datetime.strptime(Data_Solicitacao, "%Y-%m-%d").date() if (Data_Solicitacao != "") and (
            Data_Solicitacao != None) else date.today()
    Data_SolicitacaoBr = data_hoje.strftime("%d/%m/%Y")

    if Plano == None:
        r = 'Resultado'
    else:
        Valor_dia = (globals()[f"plan{Plano}"]() / 30)
        d = float(Valor_dia * float(D))
        m = float((Valor_dia / 1440) * float(M))
        Valor_Desc = d + m
        Valor_Total = round((globals()[f"plan{Plano}"]() - Valor_Desc), 2)

        r = f"Data de Simulada: {Data_SolicitacaoBr}\nSolicitação de Desconto\nPlano: {Plano}\n\nDias: {D}\nMinutos: {M}\nDesconto de: {Valor_Desc:.2f}\nValor final da fatura: {Valor_Total:.2f}\n\nIndisponibilidade: ---\nOS: ---".replace(
            ".", ",")
    return r
def CalculoA(pAtual, pNovo, pVen, Data_Solicitacao):
    data_hoje = datetime.strptime(Data_Solicitacao, "%Y-%m-%d").date() if (Data_Solicitacao != "") and (
                Data_Solicitacao != None) else date.today()
    Data_SolicitacaoBr = data_hoje.strftime("%d/%m/%Y")

    DadosVen = [
        (6, 5, 24, 25) if pVen == "5" else (11, 10, 19, 20) if pVen == "10" else (16, 15, 14, 15) if pVen == "15" else (
            21, 20, 9, 10) if pVen == "20" else (26, 25, 4, 5) if pVen == "25" else None]

    if data_hoje.day != 1:
        if data_hoje.month != 1:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= DadosVen[0][1]:
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual = (Day) * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 31 - (data_hoje.day + DadosVen[0][3])
                DayPlNovo = (RestanteDayNovo) * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month - 1, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{Data_SolicitacaoBr} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}  ".replace(".",",")

                return r
            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
            else:
                Day = data_hoje.day - DadosVen[0][1]
                DayPlAtual = (Day) * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 30 - (data_hoje.day - DadosVen[0][1])
                DayPlNovo = (RestanteDayNovo) * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{Data_SolicitacaoBr} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}".replace(".",",")

                return r
        else:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= DadosVen[0][1]:
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 31 - (data_hoje.day + DadosVen[0][3])
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, 12, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{Data_SolicitacaoBr} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}  ".replace(".",",")

                return r
            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
            else:
                Day = data_hoje.day - DadosVen[0][1]
                DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 30 - (data_hoje.day - DadosVen[0][1])
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{Data_SolicitacaoBr} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}".replace(".",",")

                return r
    else:
        if data_hoje.month != 1:
            if data_hoje.day <= DadosVen[0][1]:

                # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
                RestanteDayNovo = 31 - (data_hoje.day + DadosVen[0][3])
                DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month - 1, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{Data_SolicitacaoBr} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}  ".replace(".",",")

                return r
            else:
                Day = data_hoje.day - DadosVen[0][1]
                DayPlAtual = (Day) * (globals()[f"plan{pAtual}"]() / 30)
                RestanteDayNovo = 30 - (data_hoje.day - DadosVen[0][1])
                DayPlNovo = (RestanteDayNovo) * (globals()[f"plan{pNovo}"]() / 30)

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(data_hoje.year, data_hoje.month, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(data_hoje.year, data_hoje.month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{Data_SolicitacaoBr} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}".replace(".",",")

                return r

        else:
            Day = data_hoje.day + DadosVen[0][2]
            DayPlAtual = Day * (globals()[f"plan{pAtual}"]()/30)
            RestanteDayNovo = 31 - (data_hoje.day + DadosVen[0][3])
            DayPlNovo = RestanteDayNovo * (globals()[f"plan{pNovo}"]()/30)

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(data_hoje.year, 12, DadosVen[0][0])
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(data_hoje.year, data_hoje.month, data_hoje.day)
            AteBr = Ate.strftime("%d/%m/%Y")

            FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            r = f"Data de Simulada: {Data_SolicitacaoBr}\nDe {pAtual} para {pNovo}:\nVencimento: {pVen}\n  \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{Data_SolicitacaoBr} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}\nO valor final será: {ValorTotal:.2f}\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}\nDesconto de: {ValorTotal * 0.1:.2f}  ".replace(".",",")

            return r



def obter_contador():
    try:

        df = pd.read_csv("contador.csv")

        if not df.empty and 'contador' in df.columns:
            contador = df.iloc[0]['contador']
        else:
            contador = 0
    except FileNotFoundError:

        contador = 0

    return contador

def incrementar_contador():

    contador = obter_contador()


    contador += 1


    novo_df = pd.DataFrame({'contador': [contador]})
    novo_df.to_csv("contador.csv", index=False)

    return contador