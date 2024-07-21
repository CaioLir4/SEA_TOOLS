from blueprints.views import Telas
from database.database import db
from database.models.acess import User
from database.models.dash import Dash
from database.models.indispinibilidades import Indisponibilidade


def create_default_user():
    default_username = 'sea'
    default_password = 'sac@sea'
    default_permissions = 'Home,homepage,homepage2,       homepage3,homepage4,homepage5,  homepage6,homepage7,homepage8'

    try:
       
        if User.select().count() == 0:
    
            user = User.create(username=default_username, password=default_password, permissions=default_permissions)
           
    except IntegrityError:
   
        pass
def configura_all(app):
    configure_viewes(app)
    configure_db()

def configure_viewes(app):
    app.register_blueprint(Telas)

def configure_db():
    db.connect()
    db.create_tables([User,Dash,Indisponibilidade])
    create_default_user()
