from flask import Flask
from blueprints.views import Telas

app = Flask(__name__)
app.register_blueprint(Telas)

if __name__ == "__main__":
   app.run(debug=True)