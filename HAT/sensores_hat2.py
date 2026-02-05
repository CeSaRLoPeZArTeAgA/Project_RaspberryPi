from sense_hat import SenseHat
import os

sense = SenseHat()

def cpu_temp_c():
    # Lee la temperatura de la CPU en miligrados (Linux)
    # Ej: "42000" significa 42.0°C
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        return int(f.read()) / 1000.0

t_raw = sense.get_temperature()
t_cpu = cpu_temp_c()

# Ajuste empírico: resta una fracción de la diferencia CPU-sensor
# Puedes cambiar 1.5 por 2.0, 1.2, etc. según tu caso.
t_corr = t_raw - (t_cpu - t_raw) / 1.5

# LECTURA E IMPRESION DE DATOS DE SENSORES MEDIOAMBIENTALES
print("\n==================================")
print("LECTURA DE TEMPERATURA CORREGIDAS\n")

print("Temp cruda SenseHat [°C] =", t_raw)
print("Temp CPU [°C]            =", t_cpu)
print("Temp corregida [°C]      =", t_corr)
