FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    libgtk-3-0 \
    libgbm1 \
    libnss3 \
    libxrandr2 \
    libasound2 \
    xvfb \
    fonts-liberation \
    libx11-6 \
    libxcb1 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

RUN playwright install --with-deps chromium

ENV PYTHONPATH=/app:$PYTHONPATH

CMD ["python3", "main.py"]