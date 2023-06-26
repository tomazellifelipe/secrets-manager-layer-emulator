FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
RUN mkdir config

EXPOSE 2773

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2773"]
