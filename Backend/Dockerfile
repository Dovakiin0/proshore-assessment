FROM python:3.8-alpine

RUN pip3 freeze > requirements.txt
WORKDIR /app/backend
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5050
CMD ["python3", "app.py", "--host=0.0.0.0"]
