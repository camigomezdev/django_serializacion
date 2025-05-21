# 🐍 Django

---

## 🚀 Requerimientos

- Python 3.8 o superior
- pip
- virtualenv

---

## 🔧 Instalación

1. **Clona el repositorio**
```bash
git clone https://github.com/camigomezdev/optimizacion.git
cd optimizacion
```

2. **Crea y activa un entorno virtual**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

4. **Aplica las migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crea un superusuario**
```bash
python manage.py createsuperuser
```

6. **Creación de datos de prueba**
```bash
python manage.py create_fake_data
```

---

## ▶️ Ejecución del proyecto

1. **Levanta el servidor de desarrollo**
```bash
python manage.py runserver
```

2. **Accede en tu navegador**

```
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
```