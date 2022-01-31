FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app/

RUN python -m pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system