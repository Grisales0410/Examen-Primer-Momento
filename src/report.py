import json

def generar_reporte(resumen, ruta_salida):
    if resumen.get("bono"):
        resumen["mensaje"] = "Umbral superado, aplicar descuento corporativo 5% en próxima compra"
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(resumen, f, ensure_ascii=False, indent=2)