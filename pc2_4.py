# Gráfico de libre elección. Utilice alguno de los gráficos no utilizados en el curso de la libreria matplotlib para mostrar información que usted considere relevante de los pokemones.

import matplotlib.pyplot as plt
from aux_functions import getAllPokemons

# eggs de todos los pokemones desde el id 10, de 15 en 15
def ejercicio4():
    pokemones = getAllPokemons()
    pokemones = pokemones[::20]
    # empieza desde 9 porque al considerar a "pokemones" como una lista, su primera posicion es cero
    eggs = []
    nombres = []
    for pokemon in pokemones:
        egg = pokemon['egg']

        eggs.append(egg)
        nombres.append(pokemon['name'])

    plt.legend('')
    plt.title('DISTANCIA A LA QUE SE ENCUENTRA CADA HUEVO DE POKEMON', c='olivedrab', fontsize=20)
    plt.xlabel('Pokemones', c='teal', fontsize= 17)
    plt.ylabel('Distancia en km', c='teal', fontsize= 17)

    plt.step(nombres, eggs, c='red')
    plt.show()


ejercicio4()
