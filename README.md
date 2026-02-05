# ChatApp
Chat app module using sockets with learning purposes.

## Versión 1  ( V1 ) :

La versión 1 implementa ya con seguridad : 

	- Permite a los usuarios conectarse desde distintos dispositivos al servidor de manera 
simultanea. 

	- Implemente biblioteca thread para gestión de procesos en ejecución.

	- Almacena usuarios en línea y sus sockets correspondientes para posterior comunicación 
entre los mismos

## Versión 2 ( V2 ) : 

La verisón 2 implementea ya con seguridad : 

	- Permite a los usuarios conectarse ahora mediante su nombre de usuario lo cuál es mucho más seguro y práctico 

	- Diccionario para almacenamiento de clientes alternado : Key -> NombreUsuario Clave -> Socket

## Versión 3 ( V3 ) ( En proceso ... ): 

La versión 3 se va a enfocar en las siguientes fases : 

	- Despliegue de la aplicación en contenedores de Docker  SERVIDOR -> [X] CLIENTE -> [ ]

	- Reestructuración del sistema de ficheros del proyecto para incluir docker

	