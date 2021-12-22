# Crear un gráfico de barras en el cual se muestre los tipos de pokemon en el eje X, y la cantidad de pokemones que tienen dicho tipo como una debilidad en el eje Y.
import matplotlib.pyplot as plt

from aux_functions import getAllPokemons


def ejercicio1():
    print("Ejecutando ejercicio1")

    pokemon = getAllPokemons()
    tipo = []
    weaknesses_1 = []

    for i in range(151):
        for value in pokemon[i]["type"]:
            if value not in tipo:
                tipo.append(value)

    for i in range(151):
        for debilidad in pokemon[i]["weaknesses"]:
            weaknesses_1.append(debilidad)

    cantidad = []
    for i in range(len(tipo)):
        cantidad.append(0)
        for j in range(len(weaknesses_1)):
            if tipo[i] == weaknesses_1[j]:
                cantidad[i] = cantidad[i] + 1

    #print(len(tipo))
    colors = ["sienna", "chocolate", "saddlebrown", "peachpuff", "sandybrown", "peru", "bisque", "darkorange", "tan", "navajowhite", "orange", "burlywood", "moccasin", "wheat", "goldenrod"]

    plt.legend('')
    plt.title('CANTIDAD DE POKEMONES QUE TIENEN DICHO TIPO COMO UNA DEBILIDAD', c='olivedrab', fontsize=20)
    plt.xlabel('Tipos de pokemones', c= 'lightseagreen', fontsize=17, fontname= 'Comic Sans MS')
    plt.ylabel('Cantidad de pokemones', c= 'lightseagreen', fontsize=17, fontname='Comic Sans MS')

    plt.bar(tipo, cantidad, color=colors)
    plt.show()


ejercicio1()

