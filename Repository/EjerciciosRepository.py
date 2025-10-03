from django.db import connection
from Model.Ejercicios import Ejercicio

def getTiposRango():
    sql = """
        SELECT *
        FROM ejercicios
        """
    with connection.cursor() as cur:
        cur.execute(sql)
        filas = cur.fetchall()

    if not filas:
        return ""

    ejercicios = [Ejercicio(id=f[0], nombre=f[7]) for f in filas]
    return ejercicios