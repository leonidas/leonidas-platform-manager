FROM python:3.6
WORKDIR /usr/src/app
COPY requirements.txt requirements-production.txt /usr/src/app/
RUN groupadd -r platform && useradd -r -g platform platform && \
    pip install -U pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt -r requirements-production.txt
COPY . /usr/src/app
RUN env DEBUG=1 python manage.py collectstatic --noinput && \
    python -m compileall -q .
USER platform
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
