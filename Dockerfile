FROM python:3.12-slim

# Evita que Python escriba archivos .pyc y fuerza salida sin buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema necesarias para PostgreSQL y Pillow
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copiar el código del proyecto
COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]