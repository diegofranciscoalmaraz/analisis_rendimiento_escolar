import pandas as pd
import os

# Asegurar que existan las carpetas de salida
os.makedirs('outputs/resultados', exist_ok=True)

print("--- 1. Carga y Exploración Inicial ---")
# Cargar el dataset desde la carpeta data
df = pd.read_csv('data/StudentsPerformance.csv')

# Exploración requerida por la rúbrica
print("Número de registros y columnas:", df.shape)
print("\nTipos de datos:\n", df.dtypes)
print("\nValores faltantes:\n", df.isnull().sum())
print("\nRegistros duplicados:", df.duplicated().sum())

# Limpieza básica: Reemplazar espacios por guiones bajos en los nombres de columnas
df.columns = df.columns.str.replace(' ', '_').str.replace('/', '_')
print("\nColumnas listas para el análisis:", df.columns.tolist())

print("\n--- 2. Nuevas Variables ---")
# Variable 1: Promedio de las 3 materias
df['average_score'] = df[['math_score', 'reading_score', 'writing_score']].mean(axis=1)

# Variable 2: Clasificación de rendimiento (Criterios definidos: <60 Bajo, 60-79 Medio, 80+ Alto)
def clasificar_rendimiento(score):
    if score < 60:
        return 'Bajo'
    elif score < 80:
        return 'Medio'
    else:
        return 'Alto'

df['rendimiento'] = df['average_score'].apply(clasificar_rendimiento)
print("Muestra de nuevas variables:\n", df[['average_score', 'rendimiento']].head())

print("\n--- 3. Análisis de Datos (4 Preguntas) ---")
print("\n1. ¿Cuál de las tres áreas tiene el promedio más alto?")
print(df[['math_score', 'reading_score', 'writing_score']].mean())

print("\n2. ¿Los estudiantes que realizaron el curso de preparación presentan mejores resultados?")
print(df.groupby('test_preparation_course')['average_score'].mean())

print("\n3. ¿Existen diferencias en el rendimiento según el nivel educativo de los padres?")
print(df.groupby('parental_level_of_education')['average_score'].mean().sort_values(ascending=False))

print("\n4. ¿Qué porcentaje de estudiantes alcanza cada categoría de rendimiento?")
print((df['rendimiento'].value_counts(normalize=True) * 100).round(2), "%")
