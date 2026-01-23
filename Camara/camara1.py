# camara para vision nocturna con picamera2 y OpenCV
import cv2
from picamera2 import Picamera2

picam2 = Picamera2()

config = picam2.create_preview_configuration(
    main={"size": (1280, 720), "format": "RGB888"}
)
picam2.configure(config)
picam2.start()

# “Nocturno” aproximado: exposición alta + ganancia alta, AWB fijo
picam2.set_controls({
    "AeEnable": False,
    "ExposureTime": 30000,      # microsegundos (30 ms)
    "AnalogueGain": 10.0,
    "AwbEnable": False,
    "ColourGains": (1.0, 1.0)   # ajusta si hay dominante
})

print("Cámara en tiempo real. Presiona 'q' para salir.")

while True:
    frame = picam2.capture_array()                 # RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) # para OpenCV
    cv2.imshow("Vision nocturna (tiempo real)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
