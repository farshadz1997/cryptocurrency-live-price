FROM python:3.12
ENV PYTHONUNBUFFERED=1
WORKDIR /django_cryptocurrency_project
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt