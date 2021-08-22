import datetime
# from datetime import datetime

fecha_actual = datetime.datetime.now()
print(fecha_actual)

mi_fecha = datetime.datetime(2021, 8, 21, 10, 35, 21)
print(mi_fecha)  # 2021-08-21 10:35:21

formatear_fecha = datetime.datetime.strftime(mi_fecha, "%d/%m/%Y %H:%M:%S")
print(formatear_fecha)  # 21/08/2021 10:35:21

formatear_fecha2 = datetime.datetime.strftime(mi_fecha, "%B %d %Y %H:%M:%S")
print(formatear_fecha2)  # August 21 2021 10:35:21

fecha_cadena = "Dec 25 2019 12:06:11"
formatear_fecha3 = datetime.datetime.strptime(fecha_cadena, "%b %d %Y %H:%M:%S")
print(formatear_fecha3)  # 2019-12-25 12:06:11

dia_actual = datetime.datetime.strftime(fecha_actual, "%d")
print(dia_actual)  # 22 => cadena
print(int(dia_actual))  # 22 => entero

hora_actual = datetime.datetime.strftime(fecha_actual, "%H:%M:%S")
print(hora_actual)  # 12:21:29

print("Dia actual:", fecha_actual.day)
print("Mes actual:", fecha_actual.month)
print("Año actual:", fecha_actual.year)
print("Hora actual:", fecha_actual.hour)
print("Minuto actual:", fecha_actual.minute)
print("Segundo actual:", fecha_actual.second)
print("Microsegundo actual:", fecha_actual.microsecond)

# sumar dias
fecha_inicial = datetime.date.today()  # 2021-08-22
dias_sumar = datetime.timedelta(days=5)
dias_restar = datetime.timedelta(days=-5)
print(fecha_inicial + dias_sumar)  # 2021-08-27
print(fecha_inicial + dias_restar)  # 2021-08-17
