FROM python:3.9-slim
MAINTAINER Presslabs ping@presslabs.com

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=silver.settings

EXPOSE 8010

RUN mkdir -p /koki-pay
WORKDIR /koki-pay

COPY requirements.txt /koki-pay/requirements.txt
COPY requirements/common.txt /koki-pay/requirements/common.txt

RUN apt-get update && \
    apt-get install -y \
        libpq-dev \
        gcc \
        g++ \
        libffi-dev \
        libssl-dev \
        libjpeg-dev \
        zlib1g-dev \
        wget \
        ca-certificates \
        libxml2-dev \
        libxslt-dev \
        python3-dev && \
    pip install --no-cache-dir pip==23.3.2 && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn==20.1.0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    wget -qO- https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz | \
    tar -zxf - -C /usr/bin && \
    chown root:root /usr/bin/dockerize

RUN useradd -m -u 1000 koki && \
    mkdir -p /koki-pay/silver/migrations /koki-pay/staticfiles && \
    chown -R koki:koki /koki-pay && \
    chmod -R u+rwX /koki-pay/silver/migrations /koki-pay/staticfiles -R

COPY manage.py /koki-pay/
COPY keys.py /koki-pay/
COPY silver /koki-pay/silver
COPY settings.py /koki-pay/silver/settings.py
COPY docker-entrypoint /docker-entrypoint
RUN chmod +x /docker-entrypoint && \
    chown koki:koki /koki-pay -R && \
    chmod u+rwX /koki-pay/silver/migrations /koki-pay/staticfiles -R

USER koki

CMD ["/docker-entrypoint"]
