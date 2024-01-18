
FROM python:3.10-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements_todo.txt /app/requirements_todo.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements_todo.txt


COPY . /app
#EXPOSE 80
#
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
