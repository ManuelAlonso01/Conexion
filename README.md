# Remote-shell

## Herramienta Educativa de Administración Remota
### Arquitectura Cliente-Servidor con Sockets en Python
Este repositorio presenta un proyecto educativo que implementa una herramienta básica de administración remota utilizando una arquitectura cliente-servidor basada en sockets en Python.

El objetivo principal es comprender el funcionamiento de la comunicación en red, el intercambio de comandos entre procesos y los fundamentos técnicos detrás de herramientas de acceso remoto, desde una perspectiva de aprendizaje en redes y ciberseguridad.

## 💡Concepto
El proyecto simula un sistema de comunicación remota compuesto por dos componentes:

 - ```server.py``` (Servidor / Host remoto)
Se ejecuta en la máquina que expone el servicio y queda a la espera de conexiones entrantes. Recibe comandos enviados por el cliente y los ejecuta en el sistema.

 - ```cliente.py``` (Cliente / Controlador)
Se ejecuta en la máquina que se conecta al servidor y permite enviar comandos de forma remota a través de la conexión establecida.

Esta simulación permite estudiar:

 - Comunicación cliente-servidor

 - Uso de sockets TCP

 - Ejecución remota de comandos

 - Fundamentos de herramientas de acceso remoto

 - Riesgos de seguridad asociados a servicios expuestos en red


## 🚀 Despliegue y Ejecución
Para probar el funcionamiento, es necesario ejecutar ambos componentes en terminales separadas (pueden ser en la misma máquina o en dos diferentes).

- **1. Preparacion**: Descarga o clona el repositorio en las dos máquinas o en dos ubicaciones separadas en tu máquina local:
  
  ```bash
  git clone https://github.com/ManuelAlonso01/Remote-shell.git
  cd Remote-shell
  ```
- **2. Ejecutar el servidor**: En la máquina que actuará como host remoto, ejecutar:
  
  ```bash
  python server.py
  ```

- **3. Ejecutar el cliente**: En la máquina que actuará como controlador, ejecutar:
  ```bash
  python cliente.py
  ```
  El cliente intentará conectarse a la IP y puerto donde el servidor está escuchando.

  **Nota**: Si ejecutas ambos en la misma máquina, la IP predeterminada 127.0.0.1 con el puerto 5000 u 8000 funcionará. Si usas dos máquinas diferentes, debes editar la IP de ```server.py``` y ```cliente.py```.
  - Si no sabes cual es tu ip puedes ejecutar el comando de **windows**:
    ```bash
    ipconfig
  - o en **linux/macOS**:
    ```bash
    ifconfig
  Busca la dirección IPv4 (ej. ```192.168.1.100```). y usar un puerto como el 5000, 3000 u 8000.

## 🕹️ Uso
Una vez establecida la conexión, el cliente permite enviar comandos al servidor.
Estos comandos son ejecutados en la máquina donde se está ejecutando server.py, y la salida es devuelta al cliente.
El comportamiento es similar al de una shell remota básica, con fines exclusivamente educativos.

## ⚠️ Advertencia importante

Este proyecto fue desarrollado únicamente con fines educativos y de aprendizaje.

 - No debe utilizarse en sistemas reales sin autorización explícita.

 - Su objetivo es comprender cómo funcionan este tipo de comunicaciones para mejorar la seguridad, detectar accesos no autorizados y entender posibles vectores de ataque en redes.

El autor no se responsabiliza por usos indebidos del código.

## 📚 Tecnologías utilizadas

 - Python

 - Sockets (TCP)

 - Arquitectura Cliente-Servidor

 - Conceptos básicos de redes y sistemas

## 🎯 Objetivo educativo

 - Comprender de forma práctica:

 - Comunicación en red a bajo nivel

 - Interacción entre procesos distribuidos

 - Fundamentos técnicos de herramientas de acceso remoto

 - Implicancias de seguridad en servicios expuestos
