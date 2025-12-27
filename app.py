from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'cambia_esta_clave_secreta')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'cambia_esta_jwt_secreta')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///agrental.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Ruta de prueba para API
@app.route('/api')
def api_test():
    return {"message": "AG RENTAL Backend funcionando correctamente", "status": "OK"}

# Servir archivos estáticos (HTML, CSS, JS, imágenes)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# Ruta raíz: carga login.html
@app.route('/')
def home():
    return send_from_directory('static', 'login.html')

# Importar modelos al final (para evitar circular imports)
from models.user import User
from models.apartamento import Apartamento
from models.coche import Coche
from models.reserva import Reserva
from models.mantenimiento import Mantenimiento

# Registrar blueprint de auth (cuando lo creemos)
# from routes.auth import auth_bp
# app.register_blueprint(auth_bp)

from routes.auth import auth_bp
app.register_blueprint(auth_bp)

from routes.dashboard import dashboard_bp

app.register_blueprint(dashboard_bp)

# Logout
@app.route('/logout')
def logout():
    return '''
    <script>
      localStorage.removeItem('agrental_token');
      localStorage.removeItem('agrental_user');
      window.location.href = '/login.html';
    </script>
    '''

from routes.usuarios import usuarios_bp
app.register_blueprint(usuarios_bp)

if __name__ == '__main__':
    app.run(debug=True)