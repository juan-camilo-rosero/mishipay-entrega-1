# MishiPay

MishiPay es una billetera digital que te ofrece una experiencia para hacer tus transacciones de forma rápida y segura, todo desde la comodidad de tu navegador. Este repositorio contiene el código necesario para poner en marcha tanto el frontend como el backend de esta aplicación.

pd: No usamos la estructura sugerida en el documento porque el código no está hecho en Java

## Frontend:

En la carpeta frontend, encontrarás todo el código HTML, CSS y JavaScript necesario para la interfaz de usuario de MishiPay. Además, dentro de esta carpeta, también encontrarás estructuras de arreglo estático y pila que complementan la experiencia de usuario. Puedes acceder a la página web en funcionamiento visitando MishiPay en Vercel.

## Backend:

Dentro de la carpeta backend, encontrarás el código en Python que alimenta nuestra robusta API REST, construida con FastAPI. Aquí hay una breve descripción de lo que puedes encontrar en las subcarpetas:

    config: Contiene la configuración necesaria para la conexión con la base de datos en MongoDB.
    models: Aquí se definen las clases utilizadas tanto para las peticiones a la API REST como para las estructuras de datos de Cola y lista enlazada.
    schemas: Contiene funciones para generar la documentación de la API, lo que facilita su comprensión y uso.
    routes: Aquí se encuentran las rutas a las que se puede acceder mediante los métodos HTTP estándar (GET, POST, PUT y DELETE), implementando operaciones CRUD para la aplicación.

Además de estas carpetas, también encontrarás archivos importantes como app.py, que contiene la ejecución principal del código backend, pruebas.py, donde se realizan pruebas de las estructuras de datos, y docs.py, que contiene los metadatos necesarios para la documentación del proyecto.
