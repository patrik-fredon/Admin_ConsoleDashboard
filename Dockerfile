# Dockerfile 
FROM python:3.14.1-slim 
WORKDIR /app 
COPY . /app 
RUN pip install --no-cache-dir -r requirements.txt 
CMD ["python", "./main.py"] 
