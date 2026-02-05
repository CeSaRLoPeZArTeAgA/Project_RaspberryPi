from sense_hat import SenseHat
import math, time

sense = SenseHat()
sense.clear()

def draw_heading(angle_deg):
    cx, cy = 3.5, 3.5
    ang = math.radians(angle_deg)
    dx = math.sin(ang)
    dy = -math.cos(ang)

    for k in range(1, 4):
        x = int(round(cx + dx * k))
        y = int(round(cy + dy * k))
        if 0 <= x <= 7 and 0 <= y <= 7:
            sense.set_pixel(x, y, (0, 0, 255))

while True:
    sense.clear()
    h = sense.get_compass()
    draw_heading(h)
    time.sleep(0.2)
