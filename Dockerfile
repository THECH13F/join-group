FROM python:3.9
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "main"]
