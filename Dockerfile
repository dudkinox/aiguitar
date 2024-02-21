# ใช้ภาพพื้นฐานของ Python จาก Docker Hub
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip3 install requests

COPY . .

CMD ["python3", "./aiguitar.py"]
