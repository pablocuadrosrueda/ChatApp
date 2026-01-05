import socket 
from socket import AF_INET, SOCK_STREAM
from mensaje import Mensaje, NUM_MENSAJES
import socketserver
import sys

# VARIABLES CONSTANTES : 
ipServidor = "127.0.0.1"
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
        return False
    else:
        return True
    

def envia_mensaje(ipServer : str ,s : socket, direccion_ip : str , port : int,contenido : str):
    #Empaquetamos contenido 
    mensaje = Mensaje(ipServer,s.getsockname()[0],direccion_ip,port,contenido)
    print(mensaje)
    if(conecta_servidor(s,ipServer,port)==True):
        #Transformamos la instancia de clase en
        # un formato válido para enviar con bytes 
        s.sendall(mensaje.to_bytes())

if __name__ == "__main__":
    #Especificamos el puerto del servidor 
    port = 57876
    #Creamos el socket 
    s = crea_socket_tcp(ipServidor,puerto)
    #Escribimos el contenido 
    contenido = "Hola Mundo soy Pablo"
    #Mandamos el mensaje al destinatario
    ip = "192.168.1.33"
    r = (envia_mensaje(ipServidor,s,ip,port,contenido))
  