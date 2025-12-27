from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models.apartamento import Apartamento
from models.coche import Coche
from models.reserva import Reserva
from datetime import datetime

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/api/dashboard')

@dashboard_bp.route('', methods=['GET'])
@jwt_required()
def get_dashboard():
    # Apartamentos
    apt_total = Apartamento.query.count()
    apt_libres = Apartamento.query.filter_by(ocupacion='libre').count()
    apt_ocupados = apt_total - apt_libres
    apt_limpieza_pendiente = Apartamento.query.filter(Apartamento.limpieza_pendiente > 0).count()

    # Coches
    coche_total = Coche.query.count()
    coche_libres = Coche.query.filter_by(ocupacion='libre').count()
    coche_ocupados = coche_total - coche_libres
    coche_limpieza_pendiente = Coche.query.filter(Coche.limpieza_pendiente > 0).count()
    coche_mantenimiento_urgente = Coche.query.filter(Coche.mantenimiento_pendiente > 0).count()
    coche_documentacion_proxima = Coche.query.filter_by(documentacion_proxima=True).count()

    # Recogidas pendientes (reservas pendientes hoy)
    hoy = datetime.today().date()
    recogidas_hoy = Reserva.query.filter(Reserva.fecha_entrada == hoy, Reserva.estado_pago != 'Cancelada').count()

    return jsonify({
        "apartamentos": {
            "libres": apt_libres,
            "ocupados": apt_ocupados,
            "limpieza_pendiente": apt_limpieza_pendiente
        },
        "coches": {
            "libres": coche_libres,
            "ocupados": coche_ocupados,
            "limpieza_pendiente": coche_limpieza_pendiente,
            "mantenimiento_urgente": coche_mantenimiento_urgente,
            "documentacion_proxima": coche_documentacion_proxima
        },
        "recogidas_hoy": recogidas_hoy
    })