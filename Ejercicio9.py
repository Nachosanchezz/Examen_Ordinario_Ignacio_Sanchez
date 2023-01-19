def verificar_edad_trabajar(edad):
    if 22 <= edad <= 78:
        return True
    else:
        return False

def calcular_lunes(fecha_cumpleanios, fecha_actual):
    dias_entre_fechas = (fecha_actual - fecha_cumpleanios).days
    lunes = dias_entre_fechas // 7
    return lunes

    
