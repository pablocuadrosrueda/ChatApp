NUM_MENSAJES = 0

class Mensaje:
# ipS -> ip del servidor , ipO -> ip de origen, ipD -> ip de destino
    def __init__(self,nombreEmisor,nombreDestinatario,ipS,msg):
        self.__nombreEmisor = nombreEmisor
        self.__nombreDestinatario = nombreDestinatario
        self.__id = f"{nombreEmisor}-{NUM_MENSAJES}"
        self.__ipS = ipS
        self.__contenido = msg

    def __repr__(self):
        return (f"""
                ID -> {self.__id}
                IP SERVIDOR -> {self.__ipS}
                IP ORIGEN -> {self.__nombreEmisor}
                IP DESTINO -> {self.__nombreDestinatario}
                PUERTO -> {self.__contenido}
            """)

#Función para transformar la instancia en un paquete que se puede mandar en bytes
    def to_bytes(self):
        texto = f"{self.__ipS}|{self.__nombreEmisor}|{self.__nombreDestinatario}|{self.__contenido}"
        return texto.encode('utf-8')
