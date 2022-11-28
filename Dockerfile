FROM python:3

WORKDIR /app

COPY requirements_test.txt requirements_test.txt
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3.10", "app.py"]
