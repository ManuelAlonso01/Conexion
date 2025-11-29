import socket

# Crear socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("IP DEL SERVER", PUERTO))
print("Conectado al servidor")

# --- LOGIN ---
while True:
    password = input("Contraseña: ")
    client_socket.send(password.encode())
    respuesta = client_socket.recv(1024).decode()
    print("Servidor:", respuesta)

    if "Acceso concedido" in respuesta:
        print("Login exitoso")
        break
    elif "Demasiados intentos" in respuesta:
        print("Se agotaron los intentos, cerrando conexión...")
        client_socket.close()
        exit()

# --- SHELL REMOTA ---
while True:
    comando = input("Comando: ")
    client_socket.send(comando.encode())
    if comando.lower() == "exit":
        print("Conexión cerrada")
        break
    salida = client_socket.recv(4096).decode()
    print(salida)

client_socket.close()

