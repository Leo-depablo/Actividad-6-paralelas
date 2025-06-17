# Análisis de Rendimiento en Programación Paralela

Este repositorio contiene el código y el informe para la Actividad de Evaluación #6 de la asignatura TI3711-01-2025-3 - Programación Paralela y Distribuida.

## Descripción del Proyecto

El objetivo de este proyecto es analizar el rendimiento de un algoritmo de suma de arreglos mediante programación paralela. Se han medido métricas clave como el tiempo de ejecución, speedup y eficiencia, y se ha explorado la aplicabilidad de la Ley de Amdahl.

## Contenido del Repositorio

* **`suma_paralela.c`** (o el nombre de tu archivo C): El código fuente del algoritmo paralelo implementado con OpenMP.
* **`informe_rendimiento.docx`** (o el nombre de tu informe): El informe completo que detalla el análisis de las métricas de rendimiento, gráficos y conclusiones.

## Cómo Compilar y Ejecutar (para el código C)

1.  Asegúrate de tener un compilador C compatible con OpenMP (como GCC).
2.  Compila el código usando el siguiente comando:
    ```bash
    gcc -fopenmp suma_paralela.c -o suma_paralela
    ```
3.  Ejecuta el programa:
    ```bash
    ./suma_paralela
    ```
    El programa imprimirá los resultados del rendimiento en la consola.

## Estudiantes

* Leonardo Depablo (23-0264)
