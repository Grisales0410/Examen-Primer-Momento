from ingest import cargar_compras
from stats import estadisticas
from report import generar_reporte

def main():
    data = cargar_compras("data/compras.csv")
    resumen = estadisticas(data)
    generar_reporte(resumen, "reporte.json")
    print(resumen)

if __name__ == "__main__":
    main()