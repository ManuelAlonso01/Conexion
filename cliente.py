import socket

# 1️⃣ Crear socket y conectar
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Ejemplo: client_socket.connect(("255.255.255.255", 5000))
client_socket.connect(("IP SERVER", PUERTO))  # la misma IP y puerto del servidor
print("Conectado al servidor")

# 2️⃣ Bucle de envío de comandos
while True:
    comando = input("Comando: ")
    if comando.lower() == "exit":
        client_socket.send(comando.encode())
        break
    client_socket.send(comando.encode())  # enviar comando
    salida = client_socket.recv(4096).decode()  # recibir respuesta
    print(salida)

# 3️⃣ Cerrar conexión
client_socket.close()
