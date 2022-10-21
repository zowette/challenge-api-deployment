FROM python:3.10

ARG PORT=5000

RUN mkdir  /app

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "app.py"]