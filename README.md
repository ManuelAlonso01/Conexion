# Backdoor

## Backdoor Educativo con Python (Cliente-Servidor)
Este repositorio presenta un ejemplo simple y educativo de una puerta trasera (backdoor) implementada mediante la arquitectura Cliente-Servidor utilizando sockets de Python.

## 💡Concepto
Un backdoor es un método secreto de eludir la autenticación normal para acceder remotamente a un sistema. En este ejemplo:
- server.py (La Puerta Trasera): Actúa como el código malicioso que se ejecuta en la máquina objetivo y escucha comandos.

- cliente.py (El Atacante/Controlador): Es el programa que se ejecuta en la máquina del "atacante" para conectarse al server.py y enviarle comandos.

## 🚀 Despliegue y Ejecución
Para simular el backdoor, necesitarás ejecutar los dos componentes en diferentes terminales.

- **1. Preparacion**: Clona el repositorio en las dos máquinas o en dos ubicaciones separadas en tu máquina local:
  
  ```bash
  git clone https://github.com/ManuelAlonso01/Conexion.git
  cd Conexion

- **2. Ejecutar la Puerta Trasera (Servidor)**: En la máquina que será controlada (víctima), ejecuta el servidor (server.py). Este script se quedará a la espera de la conexión de la máquina cliente.
  
  ```bash
  python server.py

- **3. Ejecutar el Controlador (Cliente)**: En la máquina que controlará (atacante), ejecuta el cliente (cliente.py). Este intentará conectarse a la IP y puerto donde el servidor está escuchando.

  **Nota**: Si ejecutas ambos en la misma máquina, la IP predeterminada 127.0.0.1 con el puerto 5000 u 8000 funcionará. Si usas dos máquinas diferentes, debes editar la IP de ```server.py``` y ```cliente.py```.
  Si no sabes cual es tu ip puedes visitar https://whatismyipaddress.com/ y colocar la que dice **IPv4** y usar un puerto como el 5000 u 8000.

## 🕹️ Uso
Una vez que el Controlador (Cliente) se conecte exitosamente a la Puerta Trasera (Servidor), la terminal del cliente se convertirá en una shell de comandos remota.

Ahora puedes escribir comandos del sistema operativo, y estos se ejecutarán en la máquina donde se está ejecutando el ```server.py```
