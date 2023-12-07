FROM python:alpine AS build

WORKDIR /app

RUN apk add -U make

RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
