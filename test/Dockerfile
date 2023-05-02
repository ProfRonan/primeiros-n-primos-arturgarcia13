# syntax=docker/dockerfile:1
FROM python:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY test/test_main.py ./test/
COPY main.py .
CMD ["python", "-m", "unittest", "discover", "-s", "test"]

