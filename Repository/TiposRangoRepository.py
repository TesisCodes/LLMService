from django.db import connection
from Model.TiposRango import TiposRango

def getTiposRango():
    sql = """
        SELECT *
        FROM tiposrango
        """
    with connection.cursor() as cur:
        cur.execute(sql)
        filas = cur.fetchall()

    if not filas:
        return ""

    tiposRangos = [TiposRango(id=f[0], nombre=f[1]) for f in filas]
    return tiposRangos