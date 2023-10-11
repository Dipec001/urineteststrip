FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libpq-dev \
    python3-opencv

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]

