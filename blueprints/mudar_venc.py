from datetime import datetime, date
import calendar
from blueprints.planos import *


def MudarVen(vAtual, vNovo,vPlano,checkA,Data_Solicitacao):

    data_hoje = datetime.strptime(Data_Solicitacao, "%Y-%m-%d").date() if (Data_Solicitacao != "") and (Data_Solicitacao != None) else date.today()
    Data_SolicitacaoBr = data_hoje.strftime("%d-%m-%Y")

    global r

    data1 = data_hoje
    data2 = data_hoje


    if not checkA:

        MensagemFatura = f"Proxima fatura:"

        # QUANTIDADE DE DIAS NO MÊS
        Ant_quantidade_dias = calendar.monthrange(data_hoje.year - 1 if data_hoje.month == 1 else data_hoje.year, data_hoje.month - 1 if data_hoje.month != 1 else 12)[1]

        quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)[1]

        Prox_quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month+1 if data_hoje.month != 12 else 1)[1]

        # PROXIMO MÊS

        ProxAtual = (data_hoje.month % 12) + 1

        # CICLO DE 1 ATÉ 10

        Ant_IniVenc01 = date(data_hoje.year - 1 if data_hoje.month == 1 else data_hoje.year, data_hoje.month - 1 if data_hoje.month != 1 else 12, 1)
        Ant_IniVenc01Br = Ant_IniVenc01.strftime("%d/%m/%Y")
        Atu_FinalVenc30 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, data_hoje.month, quantidade_dias)
        Atu_FinalVenc30Br = Atu_FinalVenc30.strftime("%d/%m/%Y")

        IniVenc01 = date(data_hoje.year, data_hoje.month, 1)
        IniVenc01Br = IniVenc01.strftime("%d/%m/%Y")
        FinalVenc30 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, Prox_quantidade_dias)
        FinalVenc30Br = FinalVenc30.strftime("%d/%m/%Y")

        #====================================================================================================================

        # CICLO DE 11 ATÉ 10

        Ant_IniVenc11 = date(data_hoje.year - 1 if data_hoje.month == 1 else data_hoje.year, data_hoje.month - 1 if data_hoje.month != 1 else 12, 11)
        Ant_IniVenc11Br = Ant_IniVenc11.strftime("%d/%m/%Y")
        Atu_FinalVenc10 = date(data_hoje.year, data_hoje.month, 10)
        Atu_FinalVenc10Br = Atu_FinalVenc10.strftime("%d/%m/%Y")

        IniVenc11 = date(data_hoje.year, data_hoje.month, 11)
        IniVenc11Br = IniVenc11.strftime("%d/%m/%Y")
        FinalVenc10 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 10)
        FinalVenc10Br = FinalVenc10.strftime("%d/%m/%Y")

        # ====================================================================================================================


        # CICLO DE 21 ATÉ 20

        Ant_IniVenc21 = date(data_hoje.year - 1 if data_hoje.month == 1 else data_hoje.year, data_hoje.month - 1 if data_hoje.month != 1 else 12, 21)
        Ant_IniVenc21Br = Ant_IniVenc21.strftime("%d/%m/%Y")
        Atu_FinalVenc20 = date(data_hoje.year, data_hoje.month, 20)
        Atu_FinalVenc20Br = Atu_FinalVenc20.strftime("%d/%m/%Y")

        IniVenc21 = date(data_hoje.year, data_hoje.month, 21)
        IniVenc21Br = IniVenc21.strftime("%d/%m/%Y")
        FinalVenc20 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 20)
        FinalVenc20Br = FinalVenc20.strftime("%d/%m/%Y")

        # CONDIÇÕES DE TROCA DE VENCIMENTO

        if (vAtual == '5' or vAtual == '10') and (vNovo == '5' or vNovo == '10'):
            r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\nNÃO TERÁ MUDANÇA NO VALOR DA FATURA"
            return r
        elif (vAtual == '5' or vAtual == '10') and (vNovo == '15' or vNovo == '20'):
            Qtd = quantidade_dias + FinalVenc10.day
            Valor = Qtd * (globals()[f"plan{vPlano}"]()/30)
            ValorDiferenca = (Qtd-30) * (globals()[f"plan{vPlano}"]()/30)
            r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc01Br} -- {FinalVenc10Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nSão {Qtd - 30} dias -- Proporcional: {ValorDiferenca:.2f}"
            return r

        elif (vAtual == '5' or vAtual == '10') and (vNovo == '25' or vNovo == '30'):
            Qtd = quantidade_dias + FinalVenc20.day
            Valor = Qtd * (globals()[f"plan{vPlano}"]()/30)
            ValorDiferenca = (Qtd-30) * (globals()[f"plan{vPlano}"]()/30)
            r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc01Br} -- {FinalVenc20Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nSão {Qtd-30} dias -- Proporcional: {ValorDiferenca:.2f}"
            return r












        # VENCIMENTO 15 OU 20

        elif (vAtual == '15' or vAtual == '20') and (vNovo == '15' or vNovo == '20'):
            r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\nNÃO TERÁ MUDANÇA NO VALOR DA FATURA"
            return r

        elif (vAtual == '15' or vAtual == '20') and (vNovo == '25' or vNovo == '30'):
            if data_hoje.day <= IniVenc11.day:
                data1 = Ant_IniVenc11
                data2 = Atu_FinalVenc20
                Qtd = data2 - data1

                Valor = Qtd.days * (globals()[f"plan{vPlano}"]() / 30)
                ValorDiferenca = (Qtd.days - 30) * (globals()[f"plan{vPlano}"]() / 30)

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{Ant_IniVenc11Br} -- {Atu_FinalVenc20Br}. São {Qtd.days} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nSão {Qtd.days - 30} dias -- Proporcional:  {ValorDiferenca:.2f}"
                return r
            else:
                Qtd = (quantidade_dias - 10) + FinalVenc20.day
                Valor = Qtd * (globals()[f"plan{vPlano}"]()/30)
                ValorDiferenca = (Qtd-30) * (globals()[f"plan{vPlano}"]()/30)
                r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{MensagemFatura}\n{IniVenc11Br} -- {FinalVenc20Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nSão {Qtd-30} dias -- Proporcional:  {ValorDiferenca:.2f}"
                return r

        elif (vAtual == '15' or vAtual == '20') and (vNovo == '5' or vNovo == '10'):
            if data_hoje.day <= IniVenc11.day:
                data1 = Ant_IniVenc11
                data2 = Atu_FinalVenc30
                Qtd_total = data2 - data1

                Qtd = (Ant_quantidade_dias - 11)

                Valor = Qtd_total.days * (globals()[f"plan{vPlano}"]() / 30)
                Valo_plan_completo = quantidade_dias * (globals()[f"plan{vPlano}"]() / 30)
                Valor_proporcional = Qtd * (globals()[f"plan{vPlano}"]() / 30)


                r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{Ant_IniVenc11Br} -- {Atu_FinalVenc30Br}. São {Qtd_total.days} dias -- Proporcional: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nCompleta: {quantidade_dias} dias -- {Valo_plan_completo:.2f}\nProporcional: {Qtd} dias -- {Valor_proporcional:.2f}"

                return r
            else:
                Qtd = (quantidade_dias - 10)
                Valor = Qtd * (globals()[f"plan{vPlano}"]()/30)
                Valo_plan_completo = 30 * (globals()[f"plan{vPlano}"]()/30)

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{MensagemFatura}\n{IniVenc11Br} -- {FinalVenc30Br}. São {Qtd} dias -- Proporcional: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nFatura deste mês: São 30 dias -- totalizando: {Valo_plan_completo:.2f}"

                return r


        # VENCIMENTO 25 OU 30

        elif (vAtual == '25' or vAtual == '30') and (vNovo == '25' or vNovo == '30'):
            r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\nNÃO TERÁ MUDANÇA NO VALOR DA FATURA"
            return r









        elif (vAtual == '25' or vAtual == '30') and (vNovo == '15' or vNovo == '20'):
            if data_hoje.day <= IniVenc21.day:
                data1 = Ant_IniVenc21
                data2 = Atu_FinalVenc10

                Qtd_total = data2 - data1

                Valor_proporcional = Qtd_total.days * (globals()[f"plan{vPlano}"]() / 30)
                Valo_plan_completo = Qtd_total.days * (globals()[f"plan{vPlano}"]() / 30)
                Valor_total = Qtd_total.days * (globals()[f"plan{vPlano}"]() / 30)

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{Ant_IniVenc21Br} -- {Atu_FinalVenc10Br}. São {Qtd_total.days} dias -- Total: {Valor_total:.2f}\nCom desconto de 10%: {Valor_total - Valor_total * 0.1:.2f}\nDesconto de: {Valor_total * 0.1:.2f}\n\nCompleta: {Qtd_total.days} dias -- {Valo_plan_completo:.2f}\nProporcional: {Qtd_total.days} dias -- {Valor_proporcional:.2f}"

                return r
            else:
                Qtd = (quantidade_dias - 20) + FinalVenc10.day
                Valor = Qtd * (globals()[f"plan{vPlano}"]()/30)
                Valo_plan_completo = 30 * (globals()[f"plan{vPlano}"]()/30)

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{MensagemFatura}\n{IniVenc21Br} -- {FinalVenc10Br}. São {Qtd} dias -- Proporcional: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nFatura deste mês: São 30 dias -- totalizando: {Valo_plan_completo:.2f}"
                return r





        elif (vAtual == '25' or vAtual == '30') and (vNovo == '5' or vNovo == '10'):
            if data_hoje.day <= IniVenc21.day:
                data1 = Ant_IniVenc21
                data2 = Atu_FinalVenc30

                Qtd_total = data2 - data1

                Qtd = Ant_quantidade_dias - 20

                Valor_proporcional = Qtd * (globals()[f"plan{vPlano}"]() / 30)
                Valo_plan_completo = (Qtd_total.days-Qtd) * (globals()[f"plan{vPlano}"]() / 30)
                Valor_total = Qtd_total.days * (globals()[f"plan{vPlano}"]() / 30)

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{Ant_IniVenc21Br} -- {Atu_FinalVenc30Br}. São {Qtd_total.days} dias -- Proporcional: {Valor_total:.2f}\nCom desconto de 10%: {Valor_total - Valor_total * 0.1:.2f}\nDesconto de: {Valor_total * 0.1:.2f}\n\nCompleta: {Qtd_total.days-Qtd} dias -- {Valo_plan_completo:.2f}\nProporcional: {Qtd} dias -- {Valor_proporcional:.2f}"

                return r
            else:
                Qtd = (quantidade_dias - 20)
                Qtd_total = Qtd + quantidade_dias
                Valor = Qtd_total * (globals()[f"plan{vPlano}"]()/30)
                Valo_plan_completo = 30 * (globals()[f"plan{vPlano}"]()/30)

                r = f"Data de Simulada: {Data_SolicitacaoBr}\nPlano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{MensagemFatura}\n{IniVenc21Br} -- {FinalVenc30Br}. São {Qtd_total} dias -- Total: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nFatura deste mês: São 30 dias -- totalizando: {Valo_plan_completo:.2f}"
                return r

    else:
        if (vAtual == "30") or (vNovo == "30"):
            r = f"A CIDADE NÃO POSSUI ESSE VENCIMENTO!"
        else:

            DadosVenA = [(6, 5) if vNovo == "5"
            else (11, 10) if vNovo == "10"
            else (16, 15) if vNovo == "15"
            else (21, 20) if vNovo == "20"
            else (26, 25) if vNovo == "25"
            else "None"]

            if data_hoje.day <= DadosVenA[0][1]:
                    quantidade_dias = calendar.monthrange(data_hoje.year - 1 if data_hoje.month == 1 else data_hoje.year, data_hoje.month - 1 if data_hoje.month != 1 else 12)[1]
            else:
                    quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)[1]




            DadosVenB = [(6, 5, quantidade_dias, quantidade_dias+5, quantidade_dias+10, quantidade_dias+15, quantidade_dias+20) if vAtual == "5"
            else (11, 10, quantidade_dias-5, quantidade_dias, quantidade_dias+5, quantidade_dias+10, quantidade_dias+15) if vAtual == "10"
            else (16, 15, quantidade_dias-10, quantidade_dias-5, quantidade_dias, quantidade_dias+5, quantidade_dias+10) if vAtual == "15"
            else (21, 20, quantidade_dias-15, quantidade_dias-10, quantidade_dias-5, quantidade_dias, quantidade_dias+5) if vAtual == "20"
            else (26, 25, quantidade_dias-20, quantidade_dias-15, quantidade_dias-10, quantidade_dias-5, quantidade_dias) if vAtual == "25"
            else "None"]

            Contador = 2 if vNovo == "5" else 3 if vNovo == "10" else 4 if vNovo == "15" else 5 if vNovo == "20" else 6 if vNovo == "25" else "None"

            # PROXIMO MÊS

            ProxAtual = (data_hoje.month % 12) + 1


            if data_hoje.day <= DadosVenA[0][1]:

                    IniVenc = date(data_hoje.year - 1 if data_hoje.month == 1 else data_hoje.year, data_hoje.month - 1 if data_hoje.month != 1 else 12, DadosVenB[0][0])
                    IniVencBr = IniVenc.strftime("%d/%m/%Y")
                    FinalVenc = date(data_hoje.year, data_hoje.month, DadosVenA[0][1])
                    FinalVencBr = FinalVenc.strftime("%d/%m/%Y")

                    Valor = DadosVenB[0][Contador] * (globals()[f"plan{vPlano}"]() / 30)
                    ValorDiferenca = (int(vNovo) - int(vAtual)) * (globals()[f"plan{vPlano}"]() / 30)


            else:

                    IniVenc = date(data_hoje.year, data_hoje.month, DadosVenB[0][0])
                    IniVencBr = IniVenc.strftime("%d/%m/%Y")
                    FinalVenc = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, DadosVenA[0][1])
                    FinalVencBr = FinalVenc.strftime("%d/%m/%Y")

                    Valor = DadosVenB[0][Contador] * (globals()[f"plan{vPlano}"]()/30)
                    ValorDiferenca = (int(vNovo) - int(vAtual)) * (globals()[f"plan{vPlano}"]()/30)


            if vAtual == vNovo:
                r = f"Data de Simulada: {Data_SolicitacaoBr}\nNÃO TERÁ ALTERAÇÃO NA FATURA! \n"
            else:
                r = f"Data de Simulada: {Data_SolicitacaoBr}\nDo {vAtual} para {vNovo}\nPlano: {vPlano}\n\n{IniVencBr} -- {FinalVencBr}. São {DadosVenB[0][Contador]} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nProporcional de: {ValorDiferenca * -1:.2f}"

        return r


# FUNÇÃO PARA SABER QUAL CALCULO SE DEVE USAR