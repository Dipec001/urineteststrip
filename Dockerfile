FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libpq-dev \
    python3-opencv

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV PORT 8080

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Define the command to run your application using Gunicorn
CMD ["gunicorn", "urineteststrip.wsgi", "--bind", "0.0.0.0:$PORT"]


