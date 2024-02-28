from blueprints.planos import *
import calendar
from dateutil.relativedelta import relativedelta
from datetime import date, datetime, timedelta


def Calculo_cancelamento(pAtual, pVen, Data_Solicitacao, data_ati, multa):

    data_hoje = datetime.strptime(Data_Solicitacao, "%Y-%m-%d").date() if (Data_Solicitacao != "") and (Data_Solicitacao != None) else date.today()
    Data_SolicitacaoBr = data_hoje.strftime("%d-%m-%Y")

    Ant_quantidade_dias = calendar.monthrange(data_hoje.year - 1 if data_hoje.month == 1 else data_hoje.year, data_hoje.month - 1 if data_hoje.month != 1 else 12)[1]

    quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)[1]

    ProxAtual = (data_hoje.month % 12) + 1

    DadosVen = [

        (11, 10) if pVen == "15"
        else (11, 10) if pVen == "20"
        else (21, 20) if pVen == "25"
        else (21, 20) if pVen == "30"
        else (1, quantidade_dias) if pVen == "5"
        else (1, quantidade_dias) if pVen == "10"
        else (0, 0)
    ]
    if (DadosVen[0][0] == 0) or (DadosVen[0][1] == 0):
        r = "Resultado"
        return r

    elif data_ati:

        Ant_IniVenc = date(data_hoje.year - 1 if data_hoje.month == 1 else data_hoje.year, data_hoje.month - 1 if data_hoje.month != 1 else 12, DadosVen[0][0])
        Ant_IniVencBr = Ant_IniVenc.strftime("%d/%m/%Y")
        Atu_FinalVenc = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, data_hoje.month, DadosVen[0][1])
        Atu_FinalVencBr = Atu_FinalVenc.strftime("%d/%m/%Y")

        IniVenc = date(data_hoje.year, data_hoje.month, DadosVen[0][0])
        IniVencBr = IniVenc.strftime("%d/%m/%Y")
        FinalVenc = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, DadosVen[0][1])
        FinalVencBr = FinalVenc.strftime("%d/%m/%Y")

        HojeBr = data_hoje.strftime("%d/%m/%Y")

        ativa_cliente = datetime.strptime(data_ati, "%Y-%m-%d").date()
        ativa_clienteBr = ativa_cliente.strftime("%d/%m/%Y")

        venc_fidelidade = ativa_cliente + relativedelta(months= 12)
        venc_fidelidadeBr = venc_fidelidade.strftime("%d/%m/%Y")

        Prazo_30 = (data_hoje - ativa_cliente)




        if (pVen == "5") or (pVen == "10"):

            if multa:
                data1 = IniVenc
                data2 = data_hoje
                Qtd = data2 - data1

                Valor = Qtd.days * (globals()[f"plan{pAtual}"]() / 30)
                Multa_Cliente = "Dentro do prazo de 30 dias" if Prazo_30.days <= 30 else (12-(Prazo_30.days//30))*60

                r = f"Data Simulada: {Data_SolicitacaoBr}\nVencimento: {pVen}\nPlano: {pAtual}\nMulta: Sim\n\n{IniVencBr} - {HojeBr} são - {Qtd.days} dias - Total: {Valor:.2f}\n" \
                    f"Fidelidade: {ativa_clienteBr} - {venc_fidelidadeBr}\nMulta: {Multa_Cliente}"

                return r
            else:
                data1 = IniVenc
                data2 = data_hoje
                Qtd = data2 - data1

                Valor = Qtd.days * (globals()[f"plan{pAtual}"]() / 30)

                r = f"Data Simulada: {Data_SolicitacaoBr}\nVencimento: {pVen}\nPlano: {pAtual}\nMulta: Não\n\n{IniVencBr} - {HojeBr} são - {Qtd.days} dias - Total: {Valor:.2f}\n" \
                    f"Ativação: {ativa_clienteBr}"

                return r
        else:
            if multa:
                if data_hoje.day <= DadosVen[0][0]:
                    data1 = Ant_IniVenc
                    data2 = data_hoje
                    Qtd = data2 - data1

                    Valor = Qtd.days * (globals()[f"plan{pAtual}"]() / 30)
                    Multa_Cliente = "Dentro do prazo de 30 dias" if Prazo_30.days <= 30 else (11 - ((Qtd.days // 30) + 1)) * 60

                    r = f"Data Simulada: {Data_SolicitacaoBr}\nVencimento: {pVen}\nPlano: {pAtual}\nMulta: Sim\n\n{Ant_IniVencBr} - {HojeBr} são - {Qtd.days} dias - Total: {Valor:.2f}\n" \
                        f"Fidelidade: {ativa_clienteBr} - {venc_fidelidadeBr}\nMulta: {Multa_Cliente}"
                    return r
                else:
                    data1 = IniVenc
                    data2 = data_hoje
                    Qtd = data2 - data1

                    Valor = Qtd.days * (globals()[f"plan{pAtual}"]() / 30)
                    Multa_Cliente = "Dentro do prazo de 30 dias" if Prazo_30.days <= 30 else (11 - (
                                (Qtd.days // 30) + 1)) * 60

                    r = f"Data Simulada: {Data_SolicitacaoBr}\nVencimento: {pVen}\nPlano: {pAtual}\nMulta: Sim\n\n{IniVencBr} - {HojeBr} são - {Qtd.days} dias - Total: {Valor:.2f}\n" \
                        f"Fidelidade: {ativa_clienteBr} - {venc_fidelidadeBr}\nMulta: {Multa_Cliente}"
                    return r
            else:
                if data_hoje.day <= DadosVen[0][0]:
                    data1 = Ant_IniVenc
                    data2 = data_hoje
                    Qtd = data2 - data1

                    Valor = Qtd.days * (globals()[f"plan{pAtual}"]() / 30)

                    r = f"Data Simulada: {Data_SolicitacaoBr}\nVencimento: {pVen}\nPlano: {pAtual}\nMulta: Não\n\n{Ant_IniVencBr} - {HojeBr} são - {Qtd.days} dias - Total: {Valor:.2f}\n"
                    return r
                else:
                    data1 = IniVenc
                    data2 = data_hoje
                    Qtd = data2 - data1

                    Valor = Qtd.days * (globals()[f"plan{pAtual}"]() / 30)

                    r = f"Data Simulada: {Data_SolicitacaoBr}\nVencimento: {pVen}\nPlano: {pAtual}\nMulta: Não\n\n{IniVencBr} - {HojeBr} são - {Qtd.days} dias - Total: {Valor:.2f}\n"