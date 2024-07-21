from peewee import PostgresqlDatabase
from dotenv import load_dotenv
from peewee import SqliteDatabase
import os

load_dotenv()

#Descomente o #  e utilize a versão que voce desejar.

#Versão para servidor remoto, hospedagem remota. Dados de acesso ficam no servidor remoto.
#db = PostgresqlDatabase(os.getenv('DATABASE_URI', ''))



#Versão para banco de dados local, usar com Docker. Colocar dentro da string a url de acesso ao banco.
#db = PostgresqlDatabase('')



#Versão sqlite para desenvolvimento. É criado o banco autimaticamente.
db = SqliteDatabase('dbseatools.db')