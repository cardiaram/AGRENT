from app import app, db
from models.user import User
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()  # Por si acaso

    users = [
        {'username': 'empleado', 'password': 'empleado123', 'role': 'empleado'},
        {'username': 'limpieza', 'password': 'limpieza123', 'role': 'limpieza'},
        {'username': 'mantenimiento', 'password': 'mantenimiento123', 'role': 'mantenimiento'}
    ]

    for user_data in users:
        if not User.query.filter_by(username=user_data['username']).first():
            user = User(username=user_data['username'], role=user_data['role'])
            user.password_hash = generate_password_hash(user_data['password'])
            db.session.add(user)
            print(f"Usuario creado: {user_data['username']} / {user_data['password']} ({user_data['role']})")
        else:
            print(f"Usuario ya existe: {user_data['username']}")

    db.session.commit()
    print("Todos los usuarios creados correctamente")