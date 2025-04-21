# playwright_docker

Este proyecto contiene un script de automatización web utilizando Playwright para Python, empaquetado y ejecutado dentro de un contenedor Docker.

## Descripción

El script principal (`main.py`) realiza las siguientes acciones:

* Navega a la página de inicio de Playwright para Python (`https://www.playwright.dev/python/`).
* Espera unos segundos.
* Toma una captura de pantalla de la página.
* Hace clic en el enlace "Get started".
* Espera a que cambie la URL y verifica que contenga la cadena "intro".
* Espera unos segundos más.

Este proyecto también incluye la configuración necesaria para Dockerizar la aplicación, lo que permite ejecutarla de manera consistente en diferentes entornos.

## Estructura del Proyecto

playwright_docker/
├── controllers/
│   ├── init.py
│   └── conf.py         # Contiene funciones como format_time_exec y time_converter
├── .dockerignore       # Especifica archivos y directorios ignorados por Docker
├── .env                # Archivo para variables de entorno (puede estar presente)
├── .gcloudignore      # Especifica archivos ignorados por Google Cloud (puede estar presente)
├── .gitignore          # Especifica archivos ignorados por Git
├── docker-compose.yml  # (Opcional) Define la configuración para la orquestación de contenedores Docker
├── Dockerfile          # Contiene las instrucciones para construir la imagen de Docker
├── main.py             # El script principal de automatización de Playwright
├── README.md           # Este archivo
└── requirements.txt    # Lista de dependencias de Python

## Requisitos

* **Docker:** Debe tener Docker instalado en su sistema para construir y ejecutar el contenedor. Puede encontrar las instrucciones de instalación en la [documentación oficial de Docker](https://docs.docker.com/get-docker/).

## Configuración y Ejecución

1.  **Clonar el repositorio (si aplica):**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd playwright_docker
    ```

2.  **Construir la imagen de Docker:**
    Si solo estás utilizando el `Dockerfile`:
    ```bash
    docker build -t playwright_app .
    ```
    Si estás utilizando `docker-compose.yml`:
    ```bash
    docker-compose build
    ```

3.  **Ejecutar el contenedor Docker:**
    Si construiste con `docker build`:
    ```bash
    docker run playwright_app
    ```
    Si estás utilizando `docker-compose.yml`:
    ```bash
    docker-compose up
    ```

    El script se ejecutará dentro del contenedor, realizará las acciones de automatización y generará una captura de pantalla llamada `example.png` (que podría estar dentro del sistema de archivos del contenedor).

## Notas Adicionales

* Este proyecto utiliza Playwright para la automatización del navegador Chromium dentro del contenedor Docker.
* Las dependencias de Python necesarias (incluyendo `playwright`) se instalan durante la construcción de la imagen de Docker utilizando el archivo `requirements.txt`.
* Se ha configurado la variable de entorno `PYTHONPATH=/app` en el `Dockerfile` para asegurar que Python pueda encontrar los módulos locales dentro del contenedor, como el módulo `controllers`.
* Para reducir la verbosidad de los logs, se puede ajustar el nivel de logging en el script `main.py` (por ejemplo, a `logging.INFO`).
