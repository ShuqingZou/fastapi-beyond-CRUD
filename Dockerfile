FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pytest

COPY . .

EXPOSE 8000

ENV HOST 0.0.0.0

CMD ["uvicorn","src.main:app","--port","8000","--host","0.0.0.0"]
