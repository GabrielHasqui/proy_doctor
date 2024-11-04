
# App de Gestión Médica

## Descripción

La **App de Gestión Médica** es una aplicación diseñada para facilitar la administración de pacientes, doctores, citas médicas y otros aspectos relacionados con la atención médica en una clínica. La aplicación permite registrar y gestionar información detallada sobre pacientes, doctores, medicamentos, diagnósticos, exámenes médicos y más.

## Características

- **Gestión de Pacientes**: Registro y administración de información personal y médica de los pacientes.
- **Gestión de Doctores**: Registro y administración de información profesional y personal de los doctores.
- **Citas Médicas**: Programación y seguimiento de citas médicas.
- **Exámenes Médicos**: Registro y administración de exámenes médicos solicitados.
- **Servicios Adicionales**: Gestión de servicios adicionales ofrecidos durante la atención médica.
- **Costos de Atención**: Registro y administración de los costos asociados a la atención médica.

## Estructura del Proyecto

El proyecto está organizado en varios módulos, cada uno con responsabilidades específicas:

- **aplication/core**: Contiene los modelos, formularios y vistas principales de la aplicación.
- **aplication/attention**: Contiene modelos y migraciones relacionados con la atención médica, incluyendo citas y costos.
- **doctor**: Contiene scripts y configuraciones específicas para la gestión de doctores.
- **template/core**: Contiene las plantillas HTML para la interfaz de usuario, organizadas por funcionalidad.

## Tecnologías Utilizadas

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Base de Datos**: PostgreSQL

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu_usuario/app_doctor.git
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd app_doctor
    ```
3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```
4. Realiza las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```
5. Inicia el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

## Uso

- Accede a la aplicación en tu navegador web en `http://localhost:8000`.
- Utiliza el menú de navegación para acceder a las diferentes secciones de la aplicación, como la gestión de pacientes, doctores y citas médicas.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Para más información, puedes contactar al equipo de desarrollo en [correo@ejemplo.com](ghasquio@unemi.edu.ec).
