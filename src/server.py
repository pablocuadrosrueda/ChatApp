import socket 
from socket import AF_INET, SOCK_STREAM
import socketserver
import sys

# VARIABLES CONSTANTES : 
ip = "127.0.0.1"
puerto = 57876 #automático -> 0 
BUFFER_SIZE = 1024

"""
#Creación del socket 
s = socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
print(s)
"""

def crea_socket_tcp(direccion_ip : str , port : int ) -> socket:
    addr = (direccion_ip, port)
    #Creación del servidor-socket
    s = socket.create_server(addr)
    return s

def inicia_servidor( s : socket ):
    #Ponemos al servidor en escucha
    s.listen()
    puerto_real = s.getsockname()[1]
    print("Servidor escuchando en puerto:", puerto_real)
    while True:
        print(f"\nExtrayendo mensaje ... ")
        extrae_mensaje(s)


def apaga_servidor( s : socket ):
    s.close()    

def extrae_mensaje( s : socket ):
    #Aceptamos conexiones Valores de retorno de accept -> (conn, address) siendo adress (direccion_ip,puerto)
    conn, addr = s.accept()
    print(f"IP emisor: {addr[0]}")
    #Utilizamos el socket creado para la conexión con el usuario addr
    contenido = conn.recvfrom(BUFFER_SIZE)[0]
    print(f"Contenido del Mensaje: {contenido}")






if __name__ == "__main__":
    s = crea_socket_tcp(ip,puerto)
    inicia_servidor(s)