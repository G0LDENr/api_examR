from flask import Flask
from config import db, migrate, Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

# Configuración CORS
CORS(app, resources={
    r"/user/*": {
        "origins": ["http://localhost:5173"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Inicializar extensiones
db.init_app(app)
migrate.init_app(app, db)
jwt = JWTManager(app)

# Registrar blueprints
from Routes.user import user_bp
app.register_blueprint(user_bp, url_prefix='/user')

# Nueva forma de inicializar la base de datos
with app.app_context():
    db.create_all()
    print("✔ Tablas creadas correctamente")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)