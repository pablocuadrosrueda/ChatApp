import socket 
from socket import AF_INET, SOCK_STREAM
import socketserver
import sys
from mensaje import Mensaje, NUM_MENSAJES
from pprint import pprint

# VARIABLES CONSTANTES : 
ip = "127.0.0.1"
puerto = 57876 #automático -> 0 
BUFFER_SIZE = 1024

    #Diccionario de clientes en línea con : 
clientes = {}        

"""
Función para agregar un cliente en línea, devuelve True si existía previamente y False si no 
"""
def agrega_cliente( ip : str , s : socket):
    if ip not in clientes:
        clientes[ip] = s
        return True
    return False

"""
Creación del socket 
s = socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
print(s)
"""
def crea_socket_tcp(direccion_ip : str , port : int ) -> socket:
    addr = (direccion_ip, port)
    #Creación del servidor-socket
    s = socket.create_server(addr)
    return s

"""
Función de arranque para el servidor: 
    Ponemos el socket en escucha de manera indefinida ( Ctrl + C ) para interrumpir
    La función extrae_mensaje hará el trabajo de extracción 
"""
def inicia_servidor( s : socket ):
    #Ponemos al servidor en escucha
    s.listen()
    puerto_real = s.getsockname()[1]
    print("Servidor escuchando en puerto:", puerto_real)
    while True:
        print(f"\nServidor en escucha ... ")
        contenido = extrae_mensaje(s)
        print(contenido)
        envia_mensaje_a_destinatario(contenido)

"""
Función para apagar el servidor
"""
def apaga_servidor( s : socket ):
    s.close()    

"""
Función que acepta y extrae el contenido del mensaje
"""
def extrae_mensaje( s : socket ): 
    #Aceptamos conexiones Valores de retorno de accept -> (conn, address) siendo adress (direccion_ip,puerto)
    conn, addr = s.accept() 
    print(f"IP emisor: {addr[0]}") 
    #Utilizamos el socket creado para la conexión con el 
    contenido = conn.recvfrom(BUFFER_SIZE)[0] 
    #print(f"Contenido del Mensaje: {contenido}")

    #Si la Ip es nueva la almacenamos en clientes
    agrega_cliente(contenido.split(b"|")[0], conn)

    # #Devolvemos contenido 
    return contenido

"""
Función para reenviar el contenido al cliente especificado 
"""
def envia_mensaje_a_destinatario(contenido : str):
    #Extraemos el destinatario del mensaje y el contenido
    destinatario = contenido.split(b"|")[1]
    mensaje = contenido.split(b"|")[3]
    # Si tenemos el socket guardado usamos ese, si no creamos uno y envíamos
    s = None
    if destinatario in clientes:
      s = clientes[destinatario]

    if s != None:
        s.sendall(mensaje)  
    else:
        raise KeyError("El usuario destinatario no está en línea y por tanto no se puede proceder al envío de mensajes")


   



if __name__ == "__main__":
    s = crea_socket_tcp(ip,puerto)
    inicia_servidor(s)
