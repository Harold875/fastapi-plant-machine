# Resumen

Api REST con FastAPI y SqlAlchemy.

# Requisitos

- `uv` 

Es necesario tener `uv` instalado, para instalarlo revisar la documentacion de `uv`:
http://docs.astral.sh/uv/getting-started/installation/


# Variables de entorno

El proyecto utiliza las siguientes variables de entorno:

- `API_KEY`

La variable de entorno `API_KEY` se utiliza para validar la autenticación mediante el header `key`.

Las variables de entorno tienen que colocarse en el archivo `.env`.


# Pasos para iniciar el proyecto

Clonar el repositorio

```bash
git clone https://github.com/Harold875/fastapi-plant-machine.git
```

Ingresar al directorio
```bash
cd fastapi-plant-machine/
```

Instalar dependecias

```bash
uv sync
```

Iniciar el proyecto

```bash
uv run uvicorn app.main:app
```

Y ya con eso se puede visitar el http://127.0.0.1:8000

y la documentacion de la API esta en http://127.0.0.1:8000/docs



