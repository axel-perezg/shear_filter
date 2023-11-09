# Introducción

Utilizamos transformaciones geométricas para modificar la disposición espacial de los píxeles de una imagen.  Estas transformaciones se denominan *transformaciones de lámina de caucho* porque pueden considerarse análogas a "imprimir" una imagen en una lámina de caucho y luego estirar o encoger la hoja de acuerdo con un conjunto predefinido de reglas.
Las transformaciones geométricas de imágenes digitales constan de dos operaciones básicas:

- Transformación espacial de coordenadas.
- Interpolación de intensidad que asigna valores de intensidad a los píxeles transformados espacialmente.

 La transformación de coordenadas se puede expresar como

$$x$$

dónde (x, y) son las coordenadas de los píxeles de la imagen original y (x', y') corresponden a las coordenadas de los píxeles de la imagen transformada.

Por ejemplo, la transformación $$x$$ reduce la imagen a la mitad de su tamaño en ambas direcciones espaciales.

El interés principal de este proyecto son las llamadas **transformaciones afines**, las cuales incluyen scaling, translación, rotacion y shearing. 

La característica clave de una transformación afín en 2-D es que conserva puntos, líneas rectas y planos.  La ecuación anterior se puede utilizar para expresar las transformaciones que acabamos de mencionar, excepto la traslación, que requeriría agregar un vector bidimensional constante al lado derecho de la ecuación.  Sin embargo, es posible utilizar coordenadas homogéneas para expresar las cuatro transformaciones afines utilizando una sola matriz 3x3 de la siguiente manera

$$x$$

Esta transformación puede escalar, rotar, trasladar o sesgar la imagen, dependiendo de los valores de los elementos de la matriz $$A$$.

La siguiente tabla muestra los valores de la matriz usados para implementar estás transformaciones. 

Una ventaja significativa de poder realizar todas las transformaciones utilizando la representación unificada en la ecuación anterior es que proporciona el marco para concatenar una secuencia de
 operaciones.  Por ejemplo, si queremos cambiar el tamaño de una imagen, rotarla y mover el resultado a alguna ubicación, simplemente formamos una matriz de 3 × 3 igual al producto de las matrices de escala, rotación y traducción de la tabla.

## Tabla de transformaciones afines