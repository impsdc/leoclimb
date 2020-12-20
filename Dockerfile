FROM python:3.8
ENV PYTHONUNBUFFERED=1
COPY /app /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt