def verificar_edad_trabajar(edad):
    if 22 <= edad <= 78:
        return True
    else:
        return False

def calcular_lunes(fecha_cumpleaños, fecha_actual):
    dias_entre_fechas = (fecha_actual - fecha_cumpleaños).days
    lunes = dias_entre_fechas // 7
    return lunes

def numero_lunes(fecha_cumpleaños):
    hoy = datetime.datetime.now()
    edad = calcular_edad(fecha_cumpleaños)
    trabajar = verificar_edad_trabajar(edad)
    if trabajar:
        lunes = calcular_lunes(fecha_cumpleaños, hoy)
        return lunes
    else:
        return 0

fecha_cumpleaños = datetime.datetime(1998, 12, 12)
print(numero_lunes(fecha_cumpleaños))

   




