# ============================================================
#  Cívica Software  ·  TCK-4420  ·  Severidad P3
#  Sistema: RedAcopio  —  Reporte de ocupación
#  NO MODIFIQUE la seccion de datos ni el archivo de pruebas.
# ============================================================

ocupacion = [
    [4, 2, 6, 1, 3, 0],
    [0, 5, 5, 2, 7, 1],
    [8, 1, 0, 4, 2, 6],
    [3, 3, 3, 0, 0, 5],
]


def total_por_punto(m):
    """Devuelve una lista con el total recogido por cada punto (fila)."""
    totales = []
    for fila in m:
        s = 0
        for v in fila:
            s += v
        totales.append(s)
    return totales


def total_por_dia(m):
    """Devuelve una lista con el total recogido cada dia (columna)."""
    totales = []
    num_filas = len(m)
    num_columnas = len(m[0])

    for j in range(num_columnas):
        s = 0
        for i in range(num_filas):
            s += m[i][j]
        totales.append(s)
    return totales


def dia_mas_flojo(m):
    """Devuelve el indice del dia con MENOR recoleccion total."""
    totales_dias = total_por_dia(m)
    return totales_dias.index(min(totales_dias))


def puntos_inactivos(m):
    """Devuelve la cantidad total de registros (celdas) en cero."""
    contador = 0
    for fila in m:
        for v in fila:
            if v == 0:
                contador += 1
    return contador