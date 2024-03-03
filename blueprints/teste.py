from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import calendar
from planos import *

Data = date.today()
DataBr = Data.strftime("%d/%m/%Y")

DataEsp = Data + relativedelta(months= 12)

DataSub = Data - DataEsp

DataTransEsp = date(year=2004,month=1,day=14)

ProxAtual = (date.today().month % 12) + 1

quantidade_dias = calendar.monthrange(date.today().year , ProxAtual )[1]

Qtd = 12

Valor = Qtd * (globals()[f"plan{500}"]() /30)

diario = (globals()[f"plan{500}"]() /30)

VALOR = Valor + (Valor*0.02)

data_proxima = date(2024, ProxAtual,1)

print(f"{Data}\n"
      f"\n{DataEsp}\n"
      f"\n{DataSub}\n"
      f"\n{DataTransEsp}\n"
      f"\n{quantidade_dias}\n"
      f"\n {Valor}\n"
      f"\n {diario}\n"
      f"\n{ProxAtual}\n"
      f"\n {data_proxima} \n"
      f"\n {VALOR}")