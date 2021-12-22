# Visualización de datos

![](https://media.redadn.es/imagenes/pokemaster_333063.jpg)

## Descripción del proyecto

<img src="https://user-images.githubusercontent.com/90939274/146991455-e2eb1c59-6b3d-461d-81f4-78e9090c9f19.png" width="400">

¡Hola!👋 Somos el *Team Pikachu*, un grupo de científicos computacionales y nos encantan las amanecidas. En este proyecto usamos la librería `Matplotlib` para generar gráficos apartir de un archivo `JSON` donde se encuentran los datos de los Pokemones🙂.

## Nombre de los integrantes e ID de GitHub
| NOMBRE | ID |
| ------------- | ------------- |
| Capuñay Correa, Mariana Aurora  | 91635108  |
| Huarino Anchillo, Noemi Alejandra | 91573449  |
| Isidro Salazar, Leonardo Daniel  | 90939274  |
| Tovar Tolentino, Mariel Carolina  | 91162593  |



## Instrucciones para ejecutar el proyecto

```diff
+Ejercicio 1
```
En el ejercicio 1 mostramos un gráfico de barras con cada tipo de pokemon y la cantidad de pokemones que tienen este tipo como debilidad.
- Paso 1 : Creamos dos listas, `tipo` y  `weaknesses_1` para agregar los tipos y debilidades de los pokemones obtenidos.
- Paso 2 : Aplicamos un ciclo `for` a la cantidad de pokemones para así iterar en todos los tipos sin repetición, y almacenarlos en la lista correspondiente.
- Paso 3 : Aplicamos otro ciclo `for` a la cantidad de pokemones para así iterar en todas las debilidades y almacenarlos en la lista correspondiente.
- Paso 4 : Se procede a crear una lista llamada `cantidad` con la misma longitud de la lista `tipos`.
- Paso 5 : Luego aplicar un ciclo `for` para iterar en la longitud de la lista `weaknesses_1` para así realizar comparaciones entre los elementos de la listas `tipo` y  `weaknesses_1`.
- Paso 6 : Finalmente agregar 1 al elemento de la posición dada en la lista `tipo` para saber después cuántas veces se repitió.
- Paso 7 : Creamos una lista donde almacenamos los colores que va a tener cada barra.
- Paso 8 : Definimos en `plt.xlabel` y `plt.ylabel` los tipos de pokemones y cantidad de pokemones respectivamente.
- Paso 9 : Generamos el grafico de barras definiendo como parametros el tipo y cantidad de pokemones , asi como tambien el color.

![gráfico1](https://user-images.githubusercontent.com/91573449/147033611-ea3621a5-4e7c-463f-b0ab-95daa7d1c779.png)




```diff
+Ejercicio 2
```

![grafico2](https://user-images.githubusercontent.com/91573449/147022636-ead9e895-8770-4f90-8414-d82d7939c83e.png)



```diff
+Ejercicio 3
```
En el ejercicio 3 mostramos la imagen `kanto.png` con las ubicaciones de todos los pokemones cuyo `id` sea un numero primo.
- Paso 1 : Creamos la  función `es primo()` que verifica si el id del pokemon es un numero primo.
- Paso 2 : Creamos la  función `ejercicio3()` en donde obtendremos las coordenadas de los pokemones con id primo.  
- Paso 3 : Dentro de la función `ejercicio3()` creamos dos listas en donde almacenamos los valores de las coordenadas `x`, `y` , los cuales obtuvimos al utilizar la función `getLocationsByName()`.
- Paso 4 : Definimos en `plt.plot()` el valor de `x` , `y`. 
- Paso 5 : Generamos la imagen `Kanto.png` con las posiciones de los pokemones con `id` primo.

  
![grafico3](https://user-images.githubusercontent.com/90939274/147004559-41e21bf4-14e0-4320-97e9-21850e76fe22.jpg)


```diff
+Ejercicio 4
```
- Paso 1: Obtenemos la información de todos los pokemones y la almacenamos en la variable `pokemones`
- Paso 2: Realizamos un corte a la variable `pokemones`, tomamos en cuenta todos los elementos (desde el primero hasta el último) con `step=20`
- Paso 3: Creamos las listas `eggs` y `nombres`
- Paso 4: Accedemos a la información de cada pokemon con ayuda de un ciclo `for` aplicado a `pokemones`
- Paso 5: Por pokemon, agregamos el value de 'egg' en la lista 'eggs' y el value de 'name' en la lista 'nombres'.
- Paso 6: Agregamos el título (del gráfico) dentro de plt.title. Además incluimos un formato de letra diferente.
- Paso 7: Agregamos los títulos correspondientes al eje x e y, ‘Pokemones’ y ‘Distancia en km’ respectivamente.
- Paso 8: Como decidimos usar el gráfico step chart, tuvimos que hacer uso de la función 'step'. Dentro de esta incluimos como parámetros a nombres (eje x), eggs (eje y) y c=red (color).


![image](https://user-images.githubusercontent.com/91162593/147019458-18c36179-3e97-4423-b16e-6b6840908e37.png)



