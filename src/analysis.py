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
