import socket 
from socket import AF_INET, SOCK_STREAM
import socketserver
import sys
from common.mensaje import Mensaje, NUM_MENSAJES
from pprint import pprint
from threading import Thread

# VARIABLES CONSTANTES : 
ip = "0.0.0.0"
puerto = 57876 #automático -> 0 
BUFFER_SIZE = 1024

    #Diccionario de clientes en línea con clave (Nombre) -> socket : 
clientes = {}        

"""
Función para agregar un cliente en línea, devuelve True si existía previamente y False si no 
"""
def agrega_cliente( nombreUsuario : str , s : socket):
    if f"{nombreUsuario}" not in clientes:
        print(f"\nBIENVENIDO CLIENTE : [{nombreUsuario}]")
        clientes[f"{nombreUsuario}"] = s
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
        conn = acepta(s)
        #Aquí abirmos un nuevo hilo para cada usuario y 
        # llamaríamos a procesa_mensaje y posteriormente a emvia a destinatario
        t = Thread(target=procesa_mensaje,args=(conn,),daemon=True)
        #Arrancamos el nuevo hilo para el usuario
        t.start()
        
        

"""
Función para apagar el servidor
"""
def apaga_servidor( s : socket ):
    s.close()    

"""
Función que acepta al usuario en el servidor.
Devuelve el socket que se utiliza para comunicarse con el usuario de vuelta que 
será util para recibir el contenido del mensaje.
"""
def acepta( s : socket ): 
    #Aceptamos conexiones Valores de retorno de accept -> (conn, address) siendo adress (direccion_ip,puerto)
    conn,_ = s.accept() 
    #Comprobamos si es un tipo de mensaje : ONLINE ( jerga para identificar inicios de sesión. y agregamos al usuario )
    contenido = conn.recv(BUFFER_SIZE)
    if contenido.split(b'|')[0].decode('utf-8') == "ONLINE":
        #Agregamos cliente al diccionario 
        print(f"{contenido.split(b'|')[1].decode('utf-8')}")
        agrega_cliente(contenido.split(b"|")[1].decode('utf-8'),conn)
    return conn

"""
Función para extracción y procesamiento del mensaje.
Devuelve una tupla ( destinatario , contenido del mensaje )
"""

def procesa_mensaje ( s : socket ): 
    #Ya abierto el hilo para el usuario concreto, abrimos un bucle para recibir los mensajes.
    while True:
        #Utilizamos el socket creado para la conexión con el usuario
        contenido = s.recv(BUFFER_SIZE).decode('utf-8')
        #Comprobamos condición de salida
        if not contenido: 
            break
        #Procesamos el contenido del mensaje: 
        mensaje = contenido.split("|")[3]
        emisor = contenido.split("|")[1]
        destinatario = contenido.split("|")[2]

        print(f"DESTINATARIO TRAS SALIDA -> {destinatario}")
        print(f"""
                NUEVO MENSAJE DE : {emisor}
                NUEVO MENSAJE PARA : {destinatario}
                CON CONTENIDO : 
                    {mensaje}
              """)
        
        #Construimos la respuesta para el usuardio
        respuesta = f"""\nMensaje de : {emisor}
                        Contenido : 
                            {mensaje}
                    """
       
        #Reenviamos el mensaje al destinatario del mismo
        envia_mensaje_a_destinatario(destinatario,respuesta.encode('utf-8'))
    #Si salimos del bucle es porque el usuario ha abandonado la sesión por tanto 
    #cerramos tanto el hilo como su aparición en el diccionario de clientes
    del clientes[f"{emisor}"]


"""
Función para reenviar el contenido al cliente especificado 
"""
def envia_mensaje_a_destinatario(destinatario : str , mensaje : str):
    #Devolvemos la información por el socket bidireccional
    s = clientes[destinatario]
    if s != None:
        print("Enviando ...")
        s.sendall(mensaje)  
    else:
        raise KeyError("El usuario destinatario no está en línea y por tanto no se puede proceder al envío de mensajes")
   


if __name__ == "__main__":
    s = crea_socket_tcp(ip,puerto)
    inicia_servidor(s)
