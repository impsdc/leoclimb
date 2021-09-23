FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN python3 -m venv /leoclimb
COPY /app /leoclimb/app
COPY requirements.txt /leoclimb/app/requirements.txt
WORKDIR /leoclimb
RUN bin/python3 -m pip install --upgrade pip
RUN bin/pip3 install -r app/requirements.txt
RUN bin/pip3 install gunicorn