from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Mantenimiento(db.Model):
    __tablename__ = 'mantenimiento'
    id = db.Column(db.Integer, primary_key=True)
    coche_id = db.Column(db.Integer, db.ForeignKey('coche.id'), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    reportado_por = db.Column(db.String(100))
    fecha_reporte = db.Column(db.Date, default=datetime.today)
    estado = db.Column(db.String(20), default='pendiente')  # pendiente, en_curso, resuelto
    notas = db.Column(db.Text)
    urgencia = db.Column(db.String(20), default='normal')  # normal, urgente

    def __repr__(self):
        return f'<Mantenimiento {self.id} - {self.descripcion}>'