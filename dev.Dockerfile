FROM python:alpine AS build

WORKDIR /app

RUN apk add -U make

RUN python -m pip install --upgrade pip

COPY requirements.txt dev_requirements.txt .

RUN pip install --no-cache-dir -r dev_requirements.txt

COPY Makefile.common Makefile

#RUN make test

#CMD ["python", "main.py"]
#CMD "sh"