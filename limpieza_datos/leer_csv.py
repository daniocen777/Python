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
print(data2.head())
