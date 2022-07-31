FROM python:3.8-alpine

WORKDIR /app/backend
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

RUN pytest tests/

EXPOSE 5050
CMD ["python3", "app.py", "--host=0.0.0.0"]
