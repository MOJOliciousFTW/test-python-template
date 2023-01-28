FROM python:3.12.0a3-slim-bullseye

WORKDIR /app

COPY requirements_test.txt requirements_test.txt
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3.10", "app.py"]
