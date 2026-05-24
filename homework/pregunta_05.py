"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
            data = {}
            for line in file:
                parts = line.strip().split("\t")
                letter = parts[0]
                number = int(parts[1])
                if letter not in data:
                    data[letter] = [number, number]  # [min, max]
                else:
                    if number < data[letter][0]:
                        data[letter][0] = number
                    if number > data[letter][1]:
                        data[letter][1] = number
            result = [(k, v[1], v[0]) for k, v in sorted(data.items())]
    return result

if __name__ == "__main__":
    print(pregunta_05()) 
    