import requests
from Model import globals

def obtenerRecomendacion(idUsuario):
    globals.obtenerPreferenciasUsuario(idUsuario)
    prompt = f"""
    Tengo una base de datos con información de ejercicios y desempeño físico del usuario.

    A continuación te presento los datos relevantes en formato JSON:

    - **Ejercicios disponibles**:
    {globals.ejercicios_json}

    - **Tipos de rango de movimiento**:
    {globals.tiposRango_json}

    - **Articulaciones evaluadas**:
    {globals.articulaciones_json}

    - **Preferencias del usuario en tipos de rango para cada ejercicio**:
    {globals.preferencias_json}
    """

    if globals.estadisticas_ejercicios_json.__sizeof__() == 0:
        prompt += f"""
        En la última semana, el usuario **ha realizado los siguientes ejercicios**:
        {globals.estadisticas_ejercicios_json}

        Y el rendimiento de sus articulaciones fue el siguiente:
        {globals.estadisticas_articulaciones_json}
        """
    else:
        prompt += """
        En la última semana, el usuario **no ha realizado ningún ejercicio**.
        """

    prompt += """
    Con base en la información anterior, genera una **recomendación personalizada** para el usuario,
    teniendo en cuenta su rendimiento de la última semana, sus preferencias y los tipos de rango asociados a los ejercicios.

    La respuesta debe ser breve (5–8 líneas) y estar en español.
    """
    print(prompt)

    mensaje = [{"role": "user", "content": prompt}]
    payload = {
        "model": "Goosedev/luna",
        "messages": mensaje,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 256  # límite de tokens reducido
        }
    }

    resp = requests.post(f"http://10.101.136.200:11434/api/chat", json=payload)
    print(resp.json()['message']['content'])
    return resp.json()['message']['content']