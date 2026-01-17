import socket 
from socket import AF_INET, SOCK_STREAM
from mensaje import Mensaje, NUM_MENSAJES
import socketserver
import sys
from threading import Thread

# VARIABLES CONSTANTES : 
ipServidor = "127.0.0.1"
puerto = 0 #automático -> 0 
BUFFER_SIZE = 1024


"""
Función para extracción y procesamiento del mensaje.
Devuelve una tupla ( destinatario , contenido del mensaje )
"""

def procesa_mensaje ( s : socket ):    
    while True:
        #Utilizamos el socket creado para la conexión con el usuario
        contenido = s.recv(BUFFER_SIZE)
        #Procesamos el contenido del mensaje: 
        print(contenido.decode('utf-8'))

        #print(f"""
        #        NUEVO MENSAJE DE : {s.getpeername()[0]}:{s.getpeername()[1]}
        #        CON CONTENIDO : 
        #            {mensaje.decode('utf-8')}
        #    """)
    
   
"""
Función que crea el socket para la comunicación con el servidor 
"""
def crea_socket_tcp() -> socket:
    #Creación del socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s

"""
Función que gestiona la conexión al servidor
"""
def conecta_servidor(s : socket, direccion_ip : str , port : int):
    addr = (direccion_ip,port)
    #Validamos conexión
    err = s.connect(addr)
    if err:
        return False
    else:
        return True
    
"""
Función para el envío del paquete al servidor
"""
def envia_mensaje(nombreEmisor : str, nombreDestinario : str , ipServer : str ,s : socket,contenido : str):
    #Empaquetamos contenido 
    mensaje = Mensaje(nombreEmisor,nombreDestinario,ipServer,contenido)
    #Mandamos el contenido al servidor 
    s.sendall(mensaje.to_bytes())



if __name__ == "__main__":
    #Especificamos el puerto del servidor 
    port = 57876
    #Creamos el socket 
    s = crea_socket_tcp()
    #Intentamos conectar con el servidor :
    nommbreusuario = ""
    if(conecta_servidor(s,ipServidor,port)==True):
            #Aquí debemos de lanzar otro hilo que ejecute la función de escucha para recibir las respuestas
            t = Thread(target=procesa_mensaje,args=(s,),daemon=True)
            #Arrancamos el hilo
            t.start()
            #Iniciamos sesion : 
            nommbreusuario = input("Introduce tu nombre de usuario : ")
            while True:
                #Introduce el destinatario del mensaje 
                nombreDestinatario = input("Introduce el nombre del destinatario ")
                #Escribimos el contenido 
                contenido = input("Introduce el contenido del mensaje: ")
                #Conexión al servidor
                r = (envia_mensaje(nommbreusuario,nombreDestinatario,ipServidor,s,contenido))
    else:
            print("Error de conexión")
            
    