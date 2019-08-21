import pandas as pd
import os
# // --------- RESUMEN DE DATOS, DIMENSIONES Y ESTRUCTURAS --------- //
main_path = "F:/Proyectos Python/Python/datasets"
file_name = "titanic/titanic3.csv"
full_path = os.path.join(main_path, file_name)

data = pd.read_csv(full_path)
readData = data.head(10)
# print(readData)
# ---- Devolver los últimos registros ----
last_data = data.tail(8)
""" print(last_data) """

# ---- Dimensiones ----
rows_cols = data.shape  # (filas, columnas) = (1309, 14)
""" print(rows_cols) """
# ---- Nombre de columnas ----
name_columns = data.columns.values
""" print(name_columns) """

# ---- Resumen estadísticos de valores numéricos ----
# Básicos
basic_stats = data.describe()
""" print(basic_stats) """
# Tipos de datos
data_types = data.dtypes
print(data_types)
