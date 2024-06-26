from flask import Flask
from flask_cors import CORS
from auth import auth_routes
from alunos import alunos_routes
from admin import admin_routes


app = Flask(__name__)
CORS(app)

app.secret_key = 'secretkey'
app.register_blueprint(auth_routes, url_prefix='/')
app.register_blueprint(alunos_routes, url_prefix='/alunos')
app.register_blueprint(admin_routes, url_prefix='/admin')

if __name__=="__main__":
    app.run(debug=True)