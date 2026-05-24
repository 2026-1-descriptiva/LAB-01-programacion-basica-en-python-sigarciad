"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
            data = {}
            for line in file:
                parts = line.strip().split("\t")
                dict_parts = parts[4].split(",")

                for item in dict_parts:
                    key, value = item.split(":")
                    value = int(value)

                    if key not in data:
                        data[key] = [value, value]  # [min, max]
                    else:
                        if value < data[key][0]:
                            data[key][0] = value
                        if value > data[key][1]:
                            data[key][1] = value

            result = [(k, v[0], v[1]) for k, v in sorted(data.items())]
            return result


if __name__ == "__main__":
    print(pregunta_06())