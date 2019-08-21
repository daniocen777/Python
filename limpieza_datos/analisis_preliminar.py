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
""" print(data_types) """

# // --------- MISSING VALUES --------- //
data_null = pd.isnull(data["body"])
""" print(data_null) """
data_not_null = pd.notnull(data["body"])
""" print(data_not_null) """

# ravel => único arreglo de datos
sum_data_null = pd.isnull(data["body"]).values.ravel().sum()  # suma los true
""" print("Datos nulos => %d" % sum_data_null) """

sum_data_not_null = pd.notnull(
    data["body"]).values.ravel().sum()  # suma los true
""" print("Datos no nulos => %d" % sum_data_not_null) """

# // --------- BORRADO DE VALORES QUE FALTAN --------- //
# axix = 0 => borra las fila
# axix = 1 => borra las columna
""" how = all => qué fila borrar (all => si todas las filas tienen NaN ||
    any => Si al menos tiene una fila NaN) """

# // --------- COMPUTAR LOS VALORES QUE FALTAN --------- //
data2 = data  # Copia de la data
# data_without_nan = data2.fillna(0) # Filas NaN = 0
""" print(data_without_nan.head(10)) """

# Reemplazar sólo la fila "body | home.dest ..."
values = {'body': 0, 'home.dest': 'Desconocido', 'age': data2["age"].mean()}
data_without_nan = data2.fillna(value=values)
""" print(data_without_nan["age"]) """

# // --------- VARIABLES DUMMY (de ayuda) --------- //
# print(data["sex"]) # Categoría 0 => male | 1 => female
dummy_sex = pd.get_dummies(data["sex"], prefix="sex")
""" print(dummy_sex.head()) """
# Columnas
""" columns_name = data.columns.values.tolist()
print(columns_name) """
# Agregando el dummy a la data
data_without_sex = data.drop(["sex"], axis=1)  # Eliminar la columna "sex"
new_date = pd.concat([data_without_sex, dummy_sex], axis=1)  # agregar a data
""" print(new_date) """

# Función


def create_dummies(data_frame, var_name):
    dummy = pd.get_dummies(data_frame[var_name], prefix=var_name)
    data_frame_without_var = data_frame.drop(var_name, axis=1)
    new_data_frame = pd.concat([data_frame_without_var, dummy], axis=1)
    return new_data_frame

# Ejemplo => crear dummy al data2
new_data = create_dummies(data2, "sex")
columns_new_data = new_data.columns.values.tolist()
print(columns_new_data)
