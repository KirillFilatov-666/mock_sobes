FROM python:3.13-slim

WORKDIR /app

# сначала зависимости — чтобы кэшировался слой и не переустанавливались при каждом изменении кода
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# потом код
COPY . .

# команда по умолчанию при запуске контейнера
CMD ["pytest", "-v"]
