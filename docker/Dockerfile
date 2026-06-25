FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY linux_monitor/linux_monitor.py .

CMD ["python", "linux_monitor.py"]
