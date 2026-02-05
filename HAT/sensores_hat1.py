# Importa la clase SenseHat desde la librería sense_hat, esta librería permite acceder a los sensores del Sense HAT
from sense_hat import SenseHat

# Crea un objeto SenseHat para interactuar con el hardware
sense = SenseHat()

# Limpia la matriz de LEDs del Sense HAT (apaga todos los LEDs)
sense.clear()

# LECTURA E IMPRESION DE DATOS DE SENSORES MEDIOAMBIENTALES
print("\n==================================")
print("LECTURA DE SENSORES MEDIOMBIANTALE\n")

# Obtiene la presión atmosférica medida por el sensor, el valor retornado está en milibares (hPa)
pressure = sense.get_pressure()

# Muestra el valor de la presión en la consola
print("Presion[milibar] >>> ", pressure)

# Obtiene la humedad relativa del ambiente,el valor está expresado en porcentaje (%)
humidity = sense.get_humidity()

# Muestra la humedad en la consola
#print("Humedad >>> ", humidity)
print(f"Humedad[%] >>> {humidity:.3f}")

# Obtiene la temperatura ambiente usando el sensor principal, el valor está en grados Celsius
temp = sense.get_temperature()

# Muestra la temperatura en la consola
#print("Temperatura[C] >>> ", temp)
print(f"Temperatura sensor SenseHat[C] >>> {temp:.3f}")

# Obtiene la temperatura calculada a partir del sensor de presión, esta medición suele diferir ligeramente de get_temperature()
temp2 = sense.get_temperature_from_pressure()

# Muestra la segunda medición de temperatura en la consola
#print("Temperatura2[C] >>> ", temp2)
print(f"Temperatura Sensor Presion[C] >>> {temp2:.3f}")


#IMPRESION DE DATOS EN LA MATRIZ DE LEDS

# Muestra temperatura
sense.show_message(f"T:{temp:.1f}C", scroll_speed=0.10)

# Muestra humedad
sense.show_message(f"H:{humidity:.1f}%", scroll_speed=0.10)

# Muestra presión
sense.show_message(f"P:{pressure:.0f}hPa", scroll_speed=0.10)
