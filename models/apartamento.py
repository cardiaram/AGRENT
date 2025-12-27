from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Apartamento(db.Model):
    __tablename__ = 'apartamento'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.String(500), default='https://cdn.pixabay.com/photo/2016/11/18/17/46/house-1836624_1280.jpg')
    ocupacion = db.Column(db.String(20), default='libre')  # libre, ocupado
    limpieza_pendiente = db.Column(db.Integer, default=0)
    mantenimiento_pendiente = db.Column(db.Integer, default=0)
    entregas_pendientes = db.Column(db.Integer, default=0)
    precio_dia = db.Column(db.Float, default=100.0)
    descripcion = db.Column(db.Text)

    def __repr__(self):
        return f'<Apartamento {self.nombre}>'