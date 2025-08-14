import csv
from datetime import datetime

def cargar_compras(ruta):
    compras = []
    with open(ruta, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            try:
                cantidad = int(fila["cantidad"])
                precio = int(fila["precio_unitario"])
                if cantidad <= 0 or precio <= 0:
                    print(f"Advertencia: fila inválida (valores no positivos) {fila}")
                    continue
                datetime.strptime(fila["fecha"], "%Y-%m-%d")
            except (ValueError, KeyError):
                print(f"Advertencia: fila inválida (formato) {fila}")
                continue
            compras.append(fila)
    return compras