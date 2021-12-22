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
En el ejercicio 1 mostramos un grafico de barras con cada tipo de pokemon y la cantidad de pokemones que tienen este tipo como debilidad.
- Paso 1 : Creamos dos listas, en donde agregamos los tipos y las debilidades de los pokemones existentes.
- Paso 2 : Aplicamos un ciclo `for` a la lista de debilidades para almacenar en una lista contador la cantidad de pokemones que tienen como debilidad cada tipo de pokemon existente.
- Paso 3 : Creamos una lista donde almacenamos los colores que va a tener cada barra.
- Paso 4 : Definimos en `plt.xlabel` y `plt.ylabel` los tipos de pokemones y cantidad de pokemones respectivamente.
- Paso 5 : Generamos el grafico de barras definiendo como parametros el tipo y cantidad de pokemones , asi como tambien el color.
![gráfico1](https://user-images.githubusercontent.com/91573449/147019870-3046135c-1187-4a50-b7a3-12332004ddb0.png)


```diff
+Ejercicio 2
```

![grafico2](https://user-images.githubusercontent.com/91573449/147022636-ead9e895-8770-4f90-8414-d82d7939c83e.png)



```diff
+Ejercicio 3
```

En el ejercicio 3 mostramos la imagen `kanto.png` con las ubicaciones de todos los pokemones cuyo `id` sea un numero primo.
- Paso 1 : Creamos la  función `es primo()` que verifica si el id del pokemon es un numero primo.
- Paso 2 : Creamos la  función `coordenadas()` en donde obtendremos las coordenadas de los pokemones con id primo.  
- Paso 3 : Dentro de la función `coordenadas()` creamos dos listas en donde almacenamos los valores de las coordenadas `x`, `y` , los cuales obtuvimos al utilizar la función `getLocationsByName()`.
- Paso 4 : Definimos en `plt.plot()` el valor de `x` , `y`. 
- Paso 5 : Generamos la imagen de `Kanto.png` con las posiciones de los pokemones con `id` primo.
  
![grafico3](https://user-images.githubusercontent.com/90939274/147004559-41e21bf4-14e0-4320-97e9-21850e76fe22.jpg)


```diff
+Ejercicio 4
```

![image](https://user-images.githubusercontent.com/91162593/147019458-18c36179-3e97-4423-b16e-6b6840908e37.png)



