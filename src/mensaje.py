NUM_MENSAJES = 0

class Mensaje:
# ipS -> ip del servidor , ipO -> ip de origen, ipD -> ip de destino
    def __init__(self,ipS,ipO, ipD,port,msg):
        self.__id = f"{ipO}-{NUM_MENSAJES}"
        self.__ipS = ipS
        self.__ipO = ipO
        self.__ipD = ipD
        self.__port = port
        self.__contenido = msg

    def __repr__(self):
        return (f"""
                ID -> {self.__id}
                IP SERVIDOR -> {self.__ipS}
                IP ORIGEN -> {self.__ipO}
                IP DESTINO -> {self.__ipD}
                PUERTO -> {self.__port}
            """)

#Función para transformar la instancia en un paquete que se puede mandar en bytes
    def to_bytes(self):
        texto = f"{self.__ipO}|{self.__ipD}|{self.__port}|{self.__contenido}"
        return texto.encode('utf-8')
