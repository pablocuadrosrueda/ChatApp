import socket 
from socket import AF_INET, SOCK_STREAM
import socketserver
import sys

# VARIABLES CONSTANTES : 
ip = "127.0.0.1"
puerto = 0 #automático -> 0 
BUFFER_SIZE = 1024

def crea_socket_tcp(direccion_ip : str , port : int ) -> socket:
    #Creación del socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s

def conecta_servidor(s : socket, direccion_ip : str , port : int):
    addr = (direccion_ip,port)
    #Validamos conexión
    err = s.connect(addr)
    if err:
        return err
    else:
        return True
    
def envia_mensaje(s : socket, direccion_ip : str , port : int):
    if(conecta_servidor(s,direccion_ip,port)==True):
        s.sendall(b'hola mundo')

if __name__ == "__main__":
    port = 57541
    s = crea_socket_tcp(ip,puerto)
    r = (envia_mensaje(s,ip,port))
    print(r)