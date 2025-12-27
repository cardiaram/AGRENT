from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from werkzeug.security import generate_password_hash

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/api/usuarios')

@usuarios_bp.route('', methods=['GET'])
@jwt_required()
def get_usuarios():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({
            "username": user.username,
            "role": user.role
        })
    return jsonify(users_list)

@usuarios_bp.route('', methods=['POST'])
@jwt_required()
def create_usuario():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if not username or not password or not role:
        return jsonify({"error": "Faltan datos"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "El usuario ya existe"}), 400

    new_user = User(username=username, role=role)
    new_user.password_hash = generate_password_hash(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuario creado correctamente"}), 201