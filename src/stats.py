def estadisticas(data):
    resumen = {
        "total_ingresos": 0,
        "top_producto_por_ingresos": None,
        "compras_por_cliente": {},
    }

    ingresos_por_producto = {}

    for fila in data:
        cantidad = int(fila["cantidad"])
        precio = int(fila["precio_unitario"])
        ingresos = cantidad * precio

        resumen["total_ingresos"] += ingresos
        ingresos_por_producto[fila["producto"]] = ingresos_por_producto.get(fila["producto"], 0) + ingresos
        resumen["compras_por_cliente"][fila["cliente"]] = resumen["compras_por_cliente"].get(fila["cliente"], 0) + cantidad

    if ingresos_por_producto:
        resumen["top_producto_por_ingresos"] = max(ingresos_por_producto, key=ingresos_por_producto.get)

    resumen["bono"] = resumen["total_ingresos"] > 6_000_000

    return resumen