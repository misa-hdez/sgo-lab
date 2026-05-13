# Sistema relativo de referencia: unidad base de distancia y medidas relativas de progreso 

La optimización matemática consiste en seleccionar el mejor elemento de un conjunto de alternativas disponibles bajo un criterio específico.\
En problemas de optimización *black-box*, dicho conjunto no está disponible desde el inicio: se construye mediante evaluaciones en el espacio de búsqueda conforme el algoritmo explora distintas regiones de la función objetivo.

En este contexto, predecir el comportamiento de la función exige que tanto el muestreo como la interpretación de los datos sean eficientes. El reto no es solo la incertidumbre sobre la ubicación del óptimo, sino también la dificultad de establecer cómo medir el progreso hacia él.

Ante la ausencia de información analítica explícita, resulta necesario definir un sistema de referencia relativo capaz de medir el avance del proceso de optimización a partir de las relaciones locales entre las muestras evaluadas, sin depender de representaciones completas de la función objetivo.

## Mínimo local como fundamento
Para continuar nuestros análisis en un entorno *black-box* de optimización, retomaremos la definición de un mínimo local:

Un punto $x^*$ es considerado como tal si existe un valor $\delta > 0$ de modo que, para todo $x$ dentro de la región definida por $|x - x^*| \leq \delta$, se cumple que:

$$
f(x^*) \leq f(x)
$$

Es decir, dentro de una vecindad de radio $\delta$ alrededor de $x^*$, ningún punto cercano alcanza un valor menor que el de $x^*$. Esta definición resulta especialmente útil en entornos *black-box*, ya que depende únicamente de comparaciones locales y no del conocimiento explícito de la función completa.

## Sistema relativo de referencias

A partir de la definición anterior, proponemos un sistema de referencia relativo que vincula distancias en el dominio con diferencias en el codominio. Consideremos el punto de partida $x_0$ y la mejor solución conocida $x_t$, donde $f(x_t) \leq f(x_0)$ . La distancia $|x_0 - x_t|$ es una medida confiable de separación en el espacio de decisión, pero carece de significado en términos de optimización si no se asocia con la diferencia funcional $|f(x_0) - f(x_t)|$. 

En la práctica, el óptimo $x^*$ es desconocido por lo que el proceso de optimización se apoya en mejores relativos. Bajo esta condición, la mejora observada respecto a $x_t$ queda acotada por: $$|f(x_0) - f(x_t)| \leq |f(x_0) - f(x^*)|$$

Si $x_t$ pertenece a una vecindad local asociada a $x^*$, entonces minimizar la función objetivo puede reinterpretarse localmente como la maximización del descenso funcional relativo: $$|f(x_0) - f(x_t)|$$

sujeto a $$f(x^*) \leq f(x_t) \leq f(x_0)$$


## Unidad base de distancia
No obstante, determinar el radio $\delta$ asociado a un mínimo local sigue siendo un desafío incluso si se dispone de un punto de partida $x_0$. En un entorno *black-box*, esta dificultad surge porque la estructura de la función objetivo únicamente puede inferirse mediante muestreo progresivo del espacio de búsqueda.

Bajo esta perspectiva, proponemos introducir una unidad base de distancia $\delta_0$ en el dominio, utilizada como escala local de exploración alrededor de la mejor solución conocida $x_t$. Esta unidad define una vecindad operacional sobre la cual el algoritmo realiza nuevas evaluaciones con el objetivo de identificar mejoras relativas en el codominio.

En particular, se asume que dentro de la vecindad inducida por $\delta_0$ pueden existir puntos $x$ tales que:

$f(x) \leq f(x_t)$

sin requerir conocimiento explícito de la ubicación del óptimo local. De esta forma, la exploración puede interpretarse como un proceso iterativo de refinamiento local guiado por las diferencias funcionales observadas entre las muestras evaluadas.

## Conclusiones parciales

Así, el sistema relativo de referencia transforma las diferencias observadas entre dominio y codominio en una medida operacional de progreso local. A partir de una escala de exploración $\delta_0$ y de las mejoras funcionales obtenidas durante el muestreo, la exploración puede orientarse mediante información estrictamente local, sin requerir representaciones explícitas de la función objetivo.