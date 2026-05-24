"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
            data = {}
            for line in file:
                parts = line.strip().split("\t")
                key = parts[0]
                dict_parts = parts[4].split(",")
                for item in dict_parts:
                    _, value = item.split(":")
                    value = int(value)
                    if key not in data:
                        data[key] = value  # Initialize with the first value
                    else:
                        data[key] += value  # Accumulate the sum

    result = dict(sorted(data.items()))
    return result
    
if __name__ == "__main__":
    print(pregunta_12())