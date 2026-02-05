#!/bin/bash

archivo="lectura_temp.txt"
echo "   SCRIPT PARA MONITOREO DE TEMP DE CPU"
echo "Presiona cualquier tecla para salir del bucle."
# Bucle infinito
while true; do 
 #realiza la accion que quiere monitorear
 echo "Para el dia de  $(date), la temperatura es es: $(vcgencmd measure_temp) "
 lectura="$(date)__$(vcgencmd measure_temp)"
 echo "$lectura" >> "$archivo"
 # Usa read -t para esperar 1 segundo y -n1 para leer una tecla
 read -t 1 -n 1  tecla
 # Si se detecta una tecla, rompe el bucle
 if [ $? = 0 ]; then
  echo "Tecla presionada, saliendo del bucle"
  break
 fi
done




