from Model.PreferenciasUsuario import PreferenciasUsuario
from Repository import RangosArticulacionEjercicioRepository as preferenciasRepository
from Repository import TiposRangoRepository as tiposRangoRepository
from Repository import EjerciciosRepository as ejerciciosRepository
from Repository import PreferenciasUsuarioRepository as preferenciasUsuarioRepository
import requests
import json
from datetime import datetime

def insertarPreferencias(idUsuario, prescripciones):
    tiposRango = tiposRangoRepository.getTiposRango()
    if(tiposRango == "" or tiposRango == []):
        return ""
    ejercicios = ejerciciosRepository.getTiposRango()
    if(ejercicios == "" or ejercicios == []):
        return ""
    preferenciasRepository.insertarPreferencias(idUsuario, prescripciones)
    tiposRango_json = json.dumps(
        [{"idTipoRango": t.id, "nombre": t.nombre} for t in tiposRango],
        ensure_ascii=False
    )
    ejercicios_json = json.dumps(
        [{"idEjercicio": e.id, "nombre": e.nombre} for e in ejercicios],
        ensure_ascii=False
    )

    prompt = (
        f"A partir del estado físico: '{prescripciones}', "
        f"asigna un 'idTipoRango' de {tiposRango_json} "
        f"a TODOS los {ejercicios.__sizeof__()} ejercicios en {ejercicios_json}. "
        f"Ten en cuenta lo siguiente: "
        f"- Mientras más grande sea el valor de 'idTipoRango', más difícil o exigente es el ejercicio. "
        f"- Si el estado físico indica dolor o problema en alguna articulación o musculo involucrada en un ejercicio, "
        f"debes asignarle un 'idTipoRango' más bajo (más fácil/seguro). "
        f"Responde SOLO con un JSON válido, sin etiquetas, sin comentarios y sin explicaciones. "
        f"Formato esperado: "
        f"[{{\"idTipoRango\": <int>, \"idEjercicio\": <int>}}, ...] "
        f"Asegúrate de incluir TODOS los ejercicios."
    )
    print(prompt)
    messages = [{"role": "user", "content": prompt}]
    payload = {"model": "Goosedev/luna", "messages": messages, "stream": False}
    resp = requests.post(f"http://localhost:11434/api/chat", json=payload)
    print(json.loads(resp.json()['message']['content']))
    try:
        data = json.loads(resp.json()['message']['content'])
    except (TypeError, ValueError) as e:
        return "LLM"

    preferencias_list = [
        PreferenciasUsuario(
            idUsuario=idUsuario,
            idTipoRango=item["idTipoRango"],
            fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),    # fecha de hoy en formato YYYY-MM-DD
            esActiva=1,
            idEjercicio=item["idEjercicio"]
        )
        for item in data
    ]
    resultado = preferenciasUsuarioRepository.insertarPreferencias(preferencias_list)
    if(resultado):
        return data
    return ""
