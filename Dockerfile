FROM python:3.12

# Instalar dependências do sistema, incluindo LZ4
RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    liblz4-dev

# Copiar o arquivo requirements.txt
COPY requirements.txt .

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto para o container
COPY . /app

# Definir o diretório de trabalho
WORKDIR /app

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
