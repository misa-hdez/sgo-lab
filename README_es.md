SGOLab
=========================

SGOLab es un proyecto personal del programa de investigación *Towards Scalable Geometric Optimization,* que explora una reinterpretación geométrica de la optimización *black-box.* 

La hipótesis central del proyecto plantea que el proceso de optimización puede abordarse desde un espacio alternativo con menor dependencia del codominio, introduciendo una separación conceptual entre el dominio y la función objetivo. 

Bajo este enfoque, en lugar de modelar explícitamente la función, SGOLab explota la geometría del *dominio acotado* mediante la construcción de un sistema de referencia relativo que guía dinámicamente el proceso de búsqueda.


## Motivación

> *"Dadme un punto de apoyo y moveré al mundo"*
>
> — Arquímedes

> En esta sección se escribirán las motivaciones.

En términos simples, el Teorema No Free Lunch establece que ningún algoritmo es universalmente superior.


En NFL establece que para superar el rendimiento promedio, un algoritmo debe explotar las regularidades o estructura de la función. En optimización *black-box* esta estructura es invisible de antemano y solo se infiere de puntos evaluados



## Avances

Actualmente, el rendimiento del algoritmo de optimización central está siendo analizado y sometido a pruebas utilizando la suite de *benchmarking* CEC 2017 y otras funciones ampliamente conocidas.

Puedes acceder a una muestra de los datos preliminares de estas evaluaciones y otros avances métricos en el siguiente enlace: [**link**]

## Dependencias

El desarrollo, las pruebas y ejecución de los experimentos de este proyecto se apoyan en las siguientes librerías y herramientas:

- [**Mealpy**](https://github.com/thieu1995/mealpy)
- [**Opfunu**](https://github.com/thieu1995/opfunu)
- [**Benchmark Functions - A Python Library**](https://gitlab.com/luca.baronti/python_benchmark_functions)


## Disponibilidad

Debido a que el modelo matemático se encuentra en proceso de documentación formal para su publicación en *whitepapers* y revistas académicas, el acceso al código de fuente está restringido temporalmente.

Si eres investigador, deseas conocer más sobre mi trabajo o buscas una colaboración técnica, puedes contactar a través del correo:
- **Contacto:** [misa.hdez97@proton.me](mailto:misa.hdez97@proton.me)


## Pendientes 

- [ ] Finalizar la redacción del *whitepaper* y los artículos académicos correspondientes
- [ ] Preparar el código base para futuras liberaciones públicas una vez se alcance la validación académica formal


