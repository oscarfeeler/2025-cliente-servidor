import os
import time
import random


def crear_panel(filas, columnas):
    return [[random.choice([0, 1]) for _ in range(columnas)] for _ in range(filas)]


def contar_vecinas_vivas(panel, x, y):
    lineas = len(panel)
    columnas = len(panel[0])
    vecinas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0),  (1, 1)
    ]
    vivas = 0
    for dx, dy in vecinas:
        nx, ny = x + dx, y + dy
        if 0 <= nx < lineas and 0 <= ny < columnas:
            vivas += panel[nx][ny]
    return vivas


def siguiente_generacion(panel):
    lineas = len(panel)
    columnas = len(panel[0])
    nuevo_panel = [[0 for _ in range(columnas)] for _ in range(lineas)]
    for i in range(lineas):
        for j in range(columnas):
            vivas = contar_vecinas_vivas(panel, i, j)
            if panel[i][j] == 1:
                if vivas in [2, 3]:
                    nuevo_panel[i][j] = 1
            else:
                if vivas == 3:
                    nuevo_panel[i][j] = 1
    return nuevo_panel


def imprimir_panel(panel):
    os.system('cls' if os.name == 'nt' else 'clear')
    for linea in panel:
        print(' '.join("■" if celda else " " for celda in linea))


if __name__ == "__main__":
    lineas = os.get_terminal_size().lines
    columnas = int(os.get_terminal_size().columns/2) - 3

    lineas = 10
    # columnas = 10
    panel = crear_panel(lineas, columnas)
    gen = 1
    while True:
        imprimir_panel(panel)
        panel = siguiente_generacion(panel)
        time.sleep(0.3)

        gen += 1
        
def main():
    lineas = os.get_terminal_size().lines
    columnas = int(os.get_terminal_size().columns/2) - 3

    lineas = 10
    # columnas = 10
    panel = crear_panel(lineas, columnas)
    gen = 1
    #while True:
    imprimir_panel(panel)
    panel = siguiente_generacion(panel)
    time.sleep(0.3)

    gen += 1
    

    