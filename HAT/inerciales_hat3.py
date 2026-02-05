from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

def wrap_deg(a):
    """Convierte 0..360 a -180..180."""
    return (a + 180) % 360 - 180

def clamp(v, lo, hi):
    return lo if v < lo else hi if v > hi else v

def draw_bar(col, value_deg, max_deg=90, color=(0, 255, 0), zero_color=(50, 50, 50)):
    """
    Dibuja una barra vertical en la columna 'col' según value_deg.
    - max_deg define el rango: [-max_deg, max_deg] -> altura máxima.
    - 0° queda en el centro (entre filas 3 y 4).
    """
    # Limita el ángulo al rango elegido
    v = clamp(value_deg, -max_deg, max_deg)

    # Normaliza a [-1, 1]
    t = v / max_deg

    # Centro (dos píxeles para representar el "cero")
    # fila 3 (arriba del centro) y fila 4 (abajo del centro)
    sense.set_pixel(col, 3, zero_color)
    sense.set_pixel(col, 4, zero_color)

    # Cantidad de “segmentos” a encender (0..3) hacia arriba o abajo
    # (Porque desde el centro hay 3 píxeles libres arriba: 0,1,2 y 3)
    n = int(round(abs(t) * 3))

    if n == 0:
        return

    if t > 0:
        # Positivo: enciende hacia ARRIBA (filas 2,1,0)
        for k in range(1, n + 1):
            row = 3 - k
            sense.set_pixel(col, row, color)
    else:
        # Negativo: enciende hacia ABAJO (filas 5,6,7)
        for k in range(1, n + 1):
            row = 4 + k
            sense.set_pixel(col, row, color)

while True:
    o = sense.get_orientation()
    pitch = wrap_deg(o["pitch"])
    roll  = wrap_deg(o["roll"])
    yaw   = o["yaw"]

    # Consola en tiempo real
    print(f"\rPitch={pitch:7.2f}°  Roll={roll:7.2f}°  Yaw={yaw:7.2f}°", end="", flush=True)

    # Limpia y dibuja barras
    sense.clear()

    # Pitch (col 0) y Roll (col 7)
    draw_bar(col=0, value_deg=pitch, max_deg=90, color=(0, 255, 0))
    draw_bar(col=7, value_deg=roll,  max_deg=90, color=(255, 255, 0))

    # Opcional: marca el centro con un puntito en medio de la matriz
    sense.set_pixel(3, 3, (30, 30, 30))
    sense.set_pixel(4, 4, (30, 30, 30))

    time.sleep(0.1)
