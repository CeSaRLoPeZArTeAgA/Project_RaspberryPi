# Permite acceder a los sensores inerciales: acelerómetro, giróscopo y magnetómetro
from sense_hat import SenseHat

# Crea un objeto SenseHat para interactuar con el hardware
sense = SenseHat()

# Imprime un encabezado en la consola indicando que se leerán sensores inerciales
print("Sensores Inerciales\n")

# Limpia la matriz de LEDs del Sense HAT (apaga todos los LEDs)
sense.clear()

# Obtiene la orientación absoluta del Sense HAT
# Retorna un diccionario con ángulos de Euler en grados:
#  - pitch: cabeceo (rotación eje X)
#  - roll : balanceo (rotación eje Y)
#  - yaw  : guiñada (rotación eje Z)
orientation = sense.get_orientation()

# Extrae el ángulo de cabeceo y lo redondea al entero más cercano
pitch = round(orientation["pitch"])

# Extrae el ángulo de balanceo y lo redondea al entero más cercano
roll = round(orientation["roll"])

# Extrae el ángulo de guiñada y lo redondea al entero más cercano
yaw = round(orientation["yaw"])

# Muestra los tres ángulos en consola usando formato posicional
# {0} → pitch (cabeceo)
# {1} → roll  (balanceo)
# {2} → yaw   (guiñada)
print("cabeceo>{0},balanceo>{1},guino>{2}".format(pitch, roll, yaw))

