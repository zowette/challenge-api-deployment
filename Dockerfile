FROM Ubuntu:22.04
FROM python:3.10.4
FROM fastapi:0.85

RUN mkdir  /app

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]