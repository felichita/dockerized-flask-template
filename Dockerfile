# syntax=docker/dockerfile:experimental

FROM python:3-alpine

ENV HOME=/app
ENV LANG en_US.utf8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

USER root

RUN mkdir ${HOME}
WORKDIR ${HOME}

ADD app ./app
ADD wsgi.py ./
ADD etc/gunicorn.conf.py /etc/app/gunicorn.conf.py
ADD requirements.txt /tmp/requirements.txt

RUN --mount=type=ssh pip install -r /tmp/requirements.txt

RUN rm -rf /root/.cache /tmp/*

USER 1000
EXPOSE 8080

HEALTHCHECK --interval=5s --timeout=3s CMD curl --fail http://localhost:8080/health_check || exit 1

ENTRYPOINT ["gunicorn"]
CMD ["-c", "/etc/app/gunicorn.conf.py", "wsgi"]
