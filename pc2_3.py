# Mostar en el mapa de kanto.png la ubicación de todos los pokemons cuyo id es un número primo. El cálculo o verificación de si el número es primo debe realizarse en código, en otras palabras, no será aceptable que obtenga los pokemons con id primo de manera manual.
import matplotlib.pyplot as plt
from aux_functions import getAllPokemons, getLocationsByName


def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def ejercicio3():
    pokemones = getAllPokemons()
    x = []
    y = []

    for pokemon in pokemones:
        id = pokemon['id']

        if primo(id) and id != 1:
            nombre = pokemon['name']
            u = getLocationsByName(nombre)

            prim_coor = u[0]

            for p in prim_coor:
                x.append(p)

            seg_coor = u[1]
            for p in seg_coor:
                y.append(p)

    im = plt.imread("Kanto.png")
    plt.imshow(im)
    plt.title('UBICACIÓN DE LOS POKEMONES CON ID PRIMO', c='olivedrab', fontsize=20)
    plt.plot(x, y, "o", color="indigo")
    plt.show()


ejercicio3()
