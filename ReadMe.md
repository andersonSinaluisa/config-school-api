# 🚀 API Configuración Escolar

Bienvenido a la **API Configuración Escolar**, un servicio RESTful construido con **Django REST Framework** para gestionar cursos, niveles y asignaturas de una institución educativa.

---

## 📚 Descripción

Esta API permite administrar:

- 📘 **Cursos**
- 🏫 **Niveles**
- 📖 **Asignaturas**
- 📑 **Relaciones entre cursos y asignaturas**

Ideal para sistemas escolares o plataformas de gestión académica.

---

## 🌐 API Root

La vista raíz muestra los endpoints principales disponibles:

### 📥 Solicitud

GET /

pgsql
Copiar
Editar

### 📤 Respuesta

```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
json
{
    "courses": "http://127.0.0.1:8000/courses/",
    "levels": "http://127.0.0.1:8000/levels/",
    "subjects": "http://127.0.0.1:8000/subjects/",
    "course-subjects": "http://127.0.0.1:8000/course-subjects/"
}
```
🛠️ Tecnologías
🐍 Python 3.x

🌱 Django 5.x

🛡️ Django REST Framework

🎨 Bootstrap 5 (personalización de interfaz)

❤️ Opcional: TailwindCSS para estilos modernos

🚀 Instalación
1️⃣ Clona el repositorio:

```bash

git clone https://github.com/andersonSinaluisa/config-school-api
cd api-configuracion-escolar

```

2️⃣ Crea y activa un entorno virtual:

```bash
python -m venv env
source env/bin/activate  # en Linux/macOS
env\Scripts\activate     # en Windows

```


3️⃣ Instala las dependencias:

```bash
pip install -r requirements.txt
    
    
```


4️⃣ Aplica migraciones:

```bash
python manage.py migrate
  
```


5️⃣ Ejecuta el servidor:

```bash
python manage.py runserver

```

📑 Endpoints disponibles

Endpoint	Descripción
/courses/	Gestión de cursos
/levels/	Gestión de niveles académicos
/subjects/	Gestión de asignaturas
/course-subjects/	Relación de cursos con asignaturas
📃 Autenticación
Actualmente los endpoints son de acceso libre para pruebas. Puedes añadir autenticación vía token o JWT en futuras versiones.

👨‍💻 Autor
Desarrollado con ❤️ por [Tu Nombre]

📄 Licencia
Este proyecto está bajo la licencia MIT.

Puedes usarlo, modificarlo y distribuirlo libremente, siempre que se mantenga la atribución al autor original.
