"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        data = {}
        for line in file:
            parts = line.strip().split("\t")
            key = int(parts[1])
            value = parts[0]
            if key not in data:
                data[key] = [value]  # Initialize list with the first value
            else:
                if value not in data[key]:
                    data[key].append(value)
        # Sort each list in the dictionary
        for _, v in data.items():
            v.sort()

        result = sorted(data.items())
    return result

if __name__ == "__main__":
    print(pregunta_08()) 