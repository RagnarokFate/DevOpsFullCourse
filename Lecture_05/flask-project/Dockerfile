FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip

RUN pip install flask


COPY . /app


EXPOSE  5000

CMD ["python", "app.py"]

