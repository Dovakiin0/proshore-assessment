FROM python:3.8-alpine

WORKDIR /backend
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
