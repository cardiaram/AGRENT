from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.user import User
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Faltan credenciales"}), 400

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity={
            'id': user.id,
            'username': user.username,
            'rol': user.role
        })
        return jsonify({
            "success": True,
            "token": access_token,
            "usuario": {
                "username": user.username,
                "rol": user.role
            }
        }), 200

    return jsonify({"error": "Credenciales incorrectas"}), 401