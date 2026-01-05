# 📱 Chat App en Python

## 📌 Enunciado

Desarrollar una aplicación de chat que permita la comunicación en tiempo real entre múltiples usuarios, utilizando Python. La aplicación funcionará bajo una arquitectura **cliente-servidor**, permitiendo el intercambio de mensajes de texto a través de la red.

Este proyecto está pensado como práctica académica o proyecto de portfolio para afianzar conceptos de redes, concurrencia y programación en Python.

---

## 🎯 Objetivos

* Comprender el modelo **cliente-servidor**
* Utilizar **sockets TCP** en Python
* Implementar **concurrencia** (hilos o programación asíncrona)
* Gestionar múltiples usuarios conectados
* Aplicar buenas prácticas de programación y documentación

---

## 🧩 Funcionalidades

### 🖥️ Servidor

El servidor deberá:

* Escuchar conexiones entrantes en un puerto configurable
* Aceptar múltiples clientes simultáneamente
* Solicitar un **nombre de usuario** al conectarse
* Reenviar (broadcast) los mensajes a todos los clientes conectados
* Notificar cuando un usuario se conecta o se desconecta
* Manejar desconexiones inesperadas sin detener el servidor

---

### 💻 Cliente

El cliente deberá:

* Conectarse al servidor mediante IP y puerto
* Permitir al usuario ingresar su nombre
* Enviar mensajes de texto
* Recibir mensajes de otros usuarios en tiempo real
* Mostrar los mensajes con el siguiente formato:

```
[usuario] mensaje
```

---

## 🔌 Comunicación

* **Protocolo:** TCP
* **Codificación:** UTF-8
* **Longitud máxima de mensaje:** 512 caracteres
* **Formato:** Strings de texto

---

## ⚙️ Especificaciones técnicas

| Elemento          | Especificación          |
| ----------------- | ----------------------- |
| Lenguaje          | Python 3.10+            |
| Red               | Sockets TCP             |
| Concurrencia      | `threading` o `asyncio` |
| Interfaz          | Consola (CLI)           |
| Sistema operativo | Multiplataforma         |

---

## 🗂️ Estructura del proyecto

```
chat_app/
│
├── server.py      # Lógica del servidor
├── client.py      # Lógica del cliente
├── config.py      # Configuración (IP, puerto, constantes)
└── README.md      # Documentación del proyecto
```

---

## 🧠 Reglas de negocio

* No se permiten nombres de usuario duplicados
* El servidor es el único encargado de reenviar mensajes
* Los clientes no se comunican directamente entre sí
* Si un cliente escribe `/exit`, se desconecta correctamente

---

## ⭐ Funcionalidades opcionales (extras)

* Mensajes privados:

  ```
  /msg usuario mensaje
  ```
* Listar usuarios conectados:

  ```
  /users
  ```
* Historial de mensajes
* Autenticación simple (usuario / contraseña)
* Interfaz gráfica (Tkinter, PyQt, etc.)
* Cifrado básico de mensajes

---

## 🧪 Criterios de evaluación

* Funcionamiento correcto del chat
* Manejo de errores y excepciones
* Código modular, limpio y legible
* Uso adecuado de concurrencia
* Comentarios y documentación

---

## 🚀 Ejecución

1. Iniciar el servidor:

   ```bash
   python server.py
   ```

2. Iniciar uno o más clientes:

   ```bash
   python client.py
   ```

---

## 📄 Licencia

Proyecto de uso educativo. Libre de modificar y reutilizar.
