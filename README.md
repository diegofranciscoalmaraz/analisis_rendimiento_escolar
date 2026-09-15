# Análisis del Rendimiento Académico

Este proyecto realiza un análisis exploratorio sobre el desempeño de estudiantes para identificar patrones relacionados con sus resultados académicos utilizando Python.

## Dataset
* Nombre: Students Performance in Exams
* Fuente: Kaggle (https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
* Descripción: Conjunto de datos que contiene las calificaciones de matemáticas, lectura y escritura de 1000 estudiantes, así como factores demográficos (género, etnia, educación de los padres, etc.).

## Objetivo
Realizar limpieza, preprocesamiento y un análisis exploratorio de datos para descubrir qué factores (como la educación de los padres o los cursos de preparación) influyen en el promedio general del estudiante.

## Requisitos
Para ejecutar este proyecto es necesario tener Python instalado y las dependencias incluidas en el archivo requirements.txt.

## Instalación

1. Clona el repositorio:
git clone https://github.com/diegofranciscoalmaraz/analisis_rendimiento_escolar

2. Entra al proyecto:
cd analisis_rendimiento_escolar

3. Crea el entorno virtual:
python -m venv .venv

4. Activa el entorno e instala las dependencias:
pip install -r requirements.txt

## Ejecución
Para correr el análisis y generar los gráficos, ejecuta el siguiente comando en la terminal desde la raíz del proyecto:
python src/analysis.py

## Análisis realizados
1. Promedios por área de estudio (Matemáticas, Lectura y Escritura).
2. Impacto del curso de preparación en las calificaciones.
3. Influencia del nivel de educación de los padres en el rendimiento.
4. Porcentaje de alumnos divididos en categorías de rendimiento (Bajo, Medio, Alto).

## Resultados y conclusiones
* El área de lectura tiene el promedio más alto.
* Los estudiantes que completan el curso de preparación obtienen, en promedio, una calificación notablemente superior.
* Existe una correlación directa entre el nivel educativo de los padres y las calificaciones de los hijos (a mayor nivel educativo, el promedio tiende a ser superior).
* La mayoría de los estudiantes se encuentran en un rendimiento Medio.
