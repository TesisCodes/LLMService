from django.db import connection

def insertarPreferencias(idEjercicio, idUsuario):
    sql = """
        SELECT e.gesto, a.nombre, r.anguloInicial, r.anguloFinal
        FROM rangosarticulacionejercicio r
        JOIN articulacionesporejercicio ape ON ape.id = r.idArticulacionEjercicio
        JOIN ejercicios e                   ON e.id  = ape.idEjercicio
        JOIN articulaciones a               ON a.id  = ape.idArticulacion
        WHERE e.nombre = %s
        """