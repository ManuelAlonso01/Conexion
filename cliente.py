import socket
import threading

IP = "192.168.1.56"
PUERTO = 8080

def recibir_mensajes(client):
    while True:
        try:
            mensaje = client.recv(1024).decode()
            if mensaje:
                print(mensaje)
        except:
            print("Desconectado del servidor")
            client.close()
            break
        
def enviar_mensajes(client):
    while True:
        mensaje = input("Mensaje: ")
        client.send(mensaje.encode())
    

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PUERTO))
print("Conectado al servidor")

# Mandamos el nombre de usuario
username = input("Nombre de usuario: ")
client.send(username.encode())

enviar = threading.Thread(target=enviar_mensajes, args=(client,))
recivir = threading.Thread(target=recibir_mensajes, args=(client,))
enviar.start()
recivir.start()
    