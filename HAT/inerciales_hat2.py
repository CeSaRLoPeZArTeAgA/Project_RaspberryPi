from sense_hat import SenseHat
import time
import math

sense = SenseHat()
sense.clear()

def wrap_deg(a):
    """Convierte ángulos tipo 0..360 a rango -180..180 (más cómodo para mapear)."""
    return (a + 180) % 360 - 180

def clamp(v, lo, hi):
    return lo if v < lo else hi if v > hi else v

def set_line_from_center(angle_deg, length=3, color=(0, 0, 255)):
    """
    Dibuja una flecha (línea) desde el centro apuntando según yaw.
    angle_deg: 0° hacia 'arriba' de la matriz, 90° hacia la derecha.
    """
    cx, cy = 3.5, 3.5
    ang = math.radians(angle_deg)

    # Definimos 0° apuntando hacia arriba => y decrece
    dx = math.sin(ang)
    dy = -math.cos(ang)

    for k in range(1, length + 1):
        x = int(round(cx + dx * k))
        y = int(round(cy + dy * k))
        if 0 <= x <= 7 and 0 <= y <= 7:
            sense.set_pixel(x, y, color)

while True:
    o = sense.get_orientation()  # dict con 'pitch','roll','yaw' en grados
    pitch = wrap_deg(o["pitch"])
    roll  = wrap_deg(o["roll"])
    yaw   = o["yaw"]  # 0..360 está bien para “brújula”

    # --- 1) Consola en tiempo real (misma línea) ---
    # \r vuelve al inicio de la línea; end="" evita salto de línea
    print(f"\rPitch={pitch:7.2f}°  Roll={roll:7.2f}°  Yaw={yaw:7.2f}°", end="", flush=True)

    # --- 2) Indicador LED ---
    # Mapeo pitch/roll a coordenadas 0..7 (asumiendo rango útil ±90°)
    # Centro de matriz ~ (3.5,3.5)
    x = 3.5 + (roll / 90.0) * 3.5
    y = 3.5 - (pitch / 90.0) * 3.5  # signo menos: pitch positivo “sube” (y decrece)

    x = int(round(clamp(x, 0, 7)))
    y = int(round(clamp(y, 0, 7)))

    sense.clear()

    # Punto central de referencia (opcional)
    sense.set_pixel(3, 3, (30, 30, 30))
    sense.set_pixel(4, 4, (30, 30, 30))

    # Punto de inclinación: rojo
    sense.set_pixel(x, y, (255, 0, 0))

    # Flecha de yaw (rumbo): azul
    set_line_from_center(yaw, length=3, color=(0, 0, 255))

    time.sleep(0.1)
