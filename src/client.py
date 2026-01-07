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
    mensaje = Mensaje(ipServer,s.getsockname(),direccion_ip,port,contenido)
    s.sendall(mensaje.to_bytes())


def escucha(s : socket):
    s.listen()
    while True:
        conn, addr = s.accept() 
        #print(f"IP emisor: {addr[0]}:{conn.getpeername()[1]}") 
        destinatario=""
        #Utilizamos el socket creado para la conexión con el usuario
        contenido = s.recv(BUFFER_SIZE)

        #Procesamos el contenido del mensaje: 
        mensaje = contenido.split(b"|")[3]
        destinatario = contenido.split(b"|")[1]
        puerto = s.getpeername()[1]

        print(f"""
                    NUEVO MENSAJE DE : {s.getpeername()[0]}:{s.getpeername()[1]}
                    NUEVO MENSAJE PARA : {destinatario.decode('utf-8')}
                    CON CONTENIDO : 
                        {mensaje.decode('utf-8')}
                """)
        



if __name__ == "__main__":
    #Especificamos el puerto del servidor 
    port = 57876
    #Creamos el socket 
    s = crea_socket_tcp(ipServidor,puerto)
    #Intentamos conectar con el servidor : 

    if(conecta_servidor(s,ipServidor,port)==True):
            #Mandamos el mensaje al destinatario
            ip = "127.0.0.1:59920"
            while True:
                #Escribimos el contenido 
                contenido = input("Introduce el contenido del mensaje: ")
                #Conexión al servidor
                r = (envia_mensaje(ipServidor,s,ip,port,contenido))
    else:
            print("Error de conexión")
            
    