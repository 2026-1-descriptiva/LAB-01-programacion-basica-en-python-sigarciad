"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
            data = {}
            for line in file:
                parts = line.strip().split("\t")
                keys = parts[3].split(",")
                value = int(parts[1])
                for key in keys:
                    key = key.lower()
                    if key not in data:
                        data[key] = value  # Initialize with the first value
                    else:
                        data[key] += value  # Accumulate the sum

    result = {k: data[k] for k in sorted(data.keys())}
    return result
    
if __name__ == "__main__":
    print(pregunta_11())