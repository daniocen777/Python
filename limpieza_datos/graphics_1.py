# %%
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# // --------- VISUALIZACIÓN DE DATOS --------- //
main_path = "F:/Proyectos Python/Python/datasets"
data = pd.read_csv(
    main_path + "/" + "customer-churn-model/Customer Churn Model.txt")
""" Si más carga, entonces habrá más minutos de llamadas """
""" data.plot(kind="scatter", x="Day Mins", y="Day Charge") """
""" Si más carga de noche, más minutos de llamadas """
""" data.plot(kind="scatter", x="Night Mins", y="Night Charge") """

# // ---------  --------- //
# Dos variables (axs => ejes), matriz de 2*2
""" los ejes y de las subtramas apiladas verticalmente 
    tienen la misma escala cuando se usa sharey = True. """
''' figure, axs = plt.subplots(2, 2, sharex=True, sharey=True)
data.plot(kind="scatter", x="Day Mins", y="Day Charge", ax=axs[0][0]) # SubPlot
data.plot(kind="scatter", x="Night Mins", y="Night Charge", ax=axs[0][1])
data.plot(kind="scatter", x="Day Calls", y="Day Charge", ax=axs[1][0])
data.plot(kind="scatter", x="Night Calls", y="Night Charge", ax=axs[1][1]) '''

# // --------- HISTOGRAMAS DE FRECUENCIAS --------- //
# ceil => Redondeo hacia arriba
''' k = int(np.ceil(1+np.log2(3333))) # Sturges
plt.hist(data["Day Calls"], bins=k)
plt.xlabel("Número de llamdas al día")
plt.ylabel("Frecuencia")
plt.title("Histograma de Número de Llamadas al día") '''

# // --------- DIAGRAMAS DE CAKA - BOXPLOT --------- //
plt.boxplot(data["Day Calls"])
plt.ylabel("Número de llamdas diarias")
plt.title("BoxPlot de Llamadas al día")

# %%
