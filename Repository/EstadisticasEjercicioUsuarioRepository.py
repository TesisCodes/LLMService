from django.db import connection
from Model.EstadisticasEjercicioUsuario import EstadisticasEjercicioUsuario

def getEstadisticasEjercicios(idUsuario):
    sql = """
                SELECT e.fecha, e.peso, e.repeticionesrealizadas 
                FROM estadisticasejerciciousuario e 
                JOIN preferenciasusuario p on p.id = e.idpreferenciausuario
                WHERE p.idUsuario = %s AND e.fecha >= CURRENT_DATE - INTERVAL '7 days'
                """
    with connection.cursor() as cur:
        cur.execute(sql, idUsuario)
        filas = cur.fetchall()

    if not filas:
        return ""

    estadisticasEjercicio = [EstadisticasEjercicioUsuario(peso=f[1], repeticionesRealizadas=f[2]) for f in filas]
    return estadisticasEjercicio