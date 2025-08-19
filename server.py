import socket
import subprocess
import bcrypt
import json


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("TU IP", "ELEGIR PUERTO")) # Puerto recomemdado: 5000

server_socket.listen(1)
print("Esperando conexión...")


client_socket, client_address = server_socket.accept() 
print(f"Cliente conectado desde {client_address}")     


with open("usuario.json", "r") as file:
    data = json.load(file)

intentos = 3
autenticado = False

while intentos >= 0 and not autenticado:
    # Recivimos la contraseña
    password = client_socket.recv(1024).decode()  
    # Verificamos si es la que tenemos almacenada
    if bcrypt.checkpw(password.encode(), data["hash"].encode()):
        client_socket.send("Acceso concedido".encode())
        autenticado = True
    else:
        client_socket.send(f"Contraseña incorrecta le quedan {intentos} intentos".encode())
        intentos -= 1
        
        
if autenticado:
    while True:
        comando = client_socket.recv(1024).decode()  # recibir comando
        if comando.lower() == "exit":
            client_socket.close()
            break
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        salida = resultado.stdout + resultado.stderr
        client_socket.send(salida.encode())  # enviar resultado de vuelta
else:
    client_socket.send(b"ERROR: Demasiados intentos. Conexion cerrada.") 
# Cerrar conexión
client_socket.close()
server_socket.close()









