from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash




class Reserva(db.Model):
    __tablename__ = 'reserva'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)  # 'apartamento', 'coche'
    item_id = db.Column(db.Integer, nullable=False)
    cliente = db.Column(db.String(100), nullable=False)
    contacto = db.Column(db.String(100), nullable=False)
    fecha_entrada = db.Column(db.Date, nullable=False)
    hora_entrada = db.Column(db.String(10), default='15:00')
    fecha_salida = db.Column(db.Date, nullable=False)
    hora_salida = db.Column(db.String(10), default='11:00')
    dias = db.Column(db.Integer, nullable=False)
    precio_dia = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    fianza = db.Column(db.Float, default=0.0)
    pagado = db.Column(db.Float, default=0.0)
    estado_pago = db.Column(db.String(30), default='Pendiente')
    quien_recoge = db.Column(db.String(100))
    canal = db.Column(db.String(50), default='Directa')
    observaciones = db.Column(db.Text)
    qr_code = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Reserva {self.id} - {self.cliente}>'