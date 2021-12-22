# Crear un scatterplot en el cual se muestre la altura de los pokemones en centimetros en el eje X, y el peso de los pokemones en kg en el eje Y.
import matplotlib.pyplot as plt
from aux_functions import getAllPokemons, getPokemonByName, getLocationsByName, getTypesByName, getWeaknessesByName


def ejercicio2():
    # x: altura en cm
    x = []
    # y: peso en kg
    y = []

    pokemones = (getAllPokemons())  # todos los pokemones

    for pokemon in pokemones:
        # informacion_de_cada_pokemon
        altura = pokemon["height"]
        altura = float(altura.replace(' m', ''))  # altura en m y como float

        # convirtiendo en cm
        altura = round(altura * 100, 1)

        x.append(altura)  # agregando la altura

        peso = pokemon["weight"]
        peso = float(peso.replace(' kg', ''))  # peso sin kg y como float

        y.append(peso)  # agregando el peso

    csfont = {'fontname': 'Comic Sans MS'}

    # leyenda
    plt.legend('')
    plt.title('ALTURA Y PESO DE LOS POKEMONES', c='olivedrab', fontsize=23)
    plt.xlabel('Altura en cm', c='firebrick', fontsize= 19, **csfont)
    plt.ylabel('Peso en kg', c='firebrick', fontsize= 19, **csfont)

    plt.scatter(x, y, c='lightseagreen')
    plt.show()


ejercicio2()