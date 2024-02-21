# ใช้ภาพพื้นฐานของ Python จาก Docker Hub
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "./aiguitar.py"]
