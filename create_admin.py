from app import app, db
from models.user import User
from werkzeug.security import generate_password_hash
from datetime import datetime

with app.app_context():
    # Crea las tablas si no existen
    db.create_all()

    # Comprueba si el admin ya existe
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(username='admin', role='admin')
        admin.password_hash = generate_password_hash('admin123')
        db.session.add(admin)
        db.session.commit()
        print("Usuario admin creado correctamente: admin / admin123")
    else:
        print("El usuario admin ya existe")