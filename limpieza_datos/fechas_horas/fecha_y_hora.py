import datetime as dt
# Fecha y hora actual
today = dt.datetime.now()
# print(today)  # 2019-08-26 14:21:58.833483
# día
''' day = today.day
month = today.month
year = today.year
print("Año: %d" %year +  " Día: %d" %day + " Mes: %d" %month) '''

# ------------ REEMPLAZAR EL TIEMPO ------------ #
now = today.replace(minute=0, second=0, microsecond=0)
''' print(now) '''
tiempo_transcurrido = today - now
''' print(tiempo_transcurrido) '''

# ------------ DELTATIME ------------ #
# Aunetar 5 días
''' today_5_days = today + dt.timedelta(days=5)
print("Hoy es: ")
print(today)
print("Dentro de 5 días es: ")
print(today_5_days) '''

# ------------ FORMATO DE FECHAS ------------ #
hoy = dt.datetime.now()
fecha = hoy.strftime("%B %d, %Y")  # cadena
''' print(fecha) '''
fecha_cadena = "26/08/2019"
# A datetime
date_to_datetime = dt.datetime.strptime(fecha_cadena, "%d/%m/%Y")
''' print(date_to_datetime) '''

# ------------ ZONA HORARIA ------------ #
central_time = dt.timezone(dt.timedelta(hours=-6))
''' print(central_time) '''
pacific_time = dt.timezone(dt.timedelta(hours=-8))
peru_time = dt.timezone(dt.timedelta(hours=-5))
now_peru_time = dt.datetime.now(peru_time)
print(now_peru_time)
