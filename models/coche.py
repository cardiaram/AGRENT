from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Coche(db.Model):
    __tablename__ = 'coche'
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    foto = db.Column(db.String(500), default='https://cdn.pixabay.com/photo/2016/11/18/17/46/car-1836624_1280.jpg')
    ocupacion = db.Column(db.String(20), default='libre')
    limpieza_pendiente = db.Column(db.Integer, default=0)
    mantenimiento_pendiente = db.Column(db.Integer, default=0)
    documentacion_proxima = db.Column(db.Boolean, default=False)
    recogidas_pendientes = db.Column(db.Integer, default=0)
    seguro_fecha = db.Column(db.Date)
    itv_fecha = db.Column(db.Date)
    impuesto_fecha = db.Column(db.Date)
    aceite_ultima = db.Column(db.Date)
    aceite_proxima = db.Column(db.Date)
    filtros_ultima = db.Column(db.Date)
    observaciones = db.Column(db.Text)

    def __repr__(self):
        return f'<Coche {self.modelo} - {self.matricula}>'