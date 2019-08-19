import pandas as pd
import os #Sistemas operativo

main_path = "F:/Proyectos Python/Python/datasets"
file_name = "titanic/titanic3.csv"
full_path = os.path.join(main_path, file_name)

data = pd.read_csv(full_path)
readData = data.head()
#print(readData)
##### ------- EJEMPLO 2 => Leer un txt --------- #####
data2 = pd.read_csv(main_path + "/" + "customer-churn-model/Customer Churn Model.txt")
# Ver las cabeceras
headers = data2.columns.values
# Si tengo los datos separados (cabeceras en un archivo y datos en otro)
#leer cabecera
data_cols = pd.read_csv(main_path + "/" + "customer-churn-model/Customer Churn Columns.csv")
#Reetiquetado
data_col_list = data_cols["Column_Names"].tolist()
data2 = pd.read_csv(main_path + "/" + "customer-churn-model/Customer Churn Model.txt",
                    header=None, names=data_col_list)
#print(data2.head())

##### ------- EJEMPLO 3 => Leer fichero con método open --------- #####
# open ==> Lee línea a línea y no de golpe como lo hace pandas
data_3 = open(main_path + "/" + "customer-churn-model/Customer Churn Model.txt", "r")
# Extrayendo la info línea a línea
# strip => elimina espacios en blanco al inicio y final
cols = data_3.__next__().strip().split(",")
#print(cols)
n_cols = len(cols) # 21
#print("Número de columnas: " + n_cols.__str__())
cols2 = data_3.readline().strip().split(",")
counter = 0
main_dictionary = {}
for col in cols:
    main_dictionary[col] = []

for line in data_3:
    values = line.strip().split(",")
    for i in range(n_cols):
        main_dictionary[cols[i]].append(values[i])
    counter += 1

#print("El dataset tiene %d filas y %d columnas" % (counter, n_cols))
data_frame = pd.DataFrame(main_dictionary)
#print(data_frame.head())

##### ------- EJEMPLO 4 => Escritura de fichero --------- #####
in_file = main_path + "/" + "customer-churn-model/Customer Churn Model.txt"
out_file = main_path + "/" + "customer-churn-model/Tab2 Customer Churn Model.txt"
# Abriendo el fichero in y out
with open(in_file, "r") as in_file_read:
    with open(out_file, "w") as aut_file_write:
        for line in in_file_read:
            fields = line.strip().split(",")
            aut_file_write.write("\t".join(fields)) # Tabulador
            aut_file_write.write("\n") # Salto de línea

# Leyendo el out_file
data_frame_4 = pd.read_csv(out_file, sep="\t")
#print(data_frame_4)

##### ------- EJEMPLO 5 => Leer fichero en la web --------- #####
medals_url = "http://winterolympicsmedals.com/medals.csv"
medals_data = pd.read_csv(medals_url)
#print(medals_data.head())

##### ------- EJEMPLO 6 => Leer fichero excel --------- #####
file_name_titanic_excel = "titanic/titanic3.xls"
# pd.read_excel("ubicación", "nombre_pestaña => hoja)
read_excel = pd.read_excel(main_path + "/" + file_name_titanic_excel, "titanic3")
# Convertir a dataframe => a csv | excel | json | etc
read_excel.to_csv(main_path + "/titanic/titanic_daniel.csv")
read_excel.to_excel(main_path + "/titanic/titanic_daniel.xls")
read_excel.to_json(main_path + "/titanic/titanic_daniel.json")




