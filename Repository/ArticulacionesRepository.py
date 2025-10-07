from django.db import connection

from Model.Articulaciones import Articulaciones


def getArticulaciones():
    sql = """
            SELECT *
            FROM articulaciones
            """
    with connection.cursor() as cur:
        cur.execute(sql)
        filas = cur.fetchall()

    if not filas:
        return ""

    articulaciones = [Articulaciones(id=f[0], nombre=f[1]) for f in filas]
    return articulaciones
