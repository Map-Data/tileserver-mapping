FROM docker.io/debian:buster-slim

RUN apt update
RUN apt install -y --no-install-recommends pipenv uwsgi uwsgi-plugin-python3 python3-psycopg2 python3-setuptools \
    nginx supervisor

# install project dependencies and add sources
ADD Pipfile Pipfile.lock /app/src/
WORKDIR /app/src
RUN pipenv install --system --deploy --ignore-pipfile
ADD . /app/src/

# put configuration in correct places
RUN mkdir -p /app/config
RUN cp /app/src/tileservermapping/settings.py.example /app/config/settings.py
RUN ln -sf /app/config/settings.py /app/src/tileservermapping/settings.py
RUN ln -s /app/src/docker/uwsgi.ini /etc/uwsgi/tileservermapping.ini
RUN ln -s /app/src/docker/supervisor.conf /etc/supervisor/conf.d/app.conf
RUN ln -sf /app/src/docker/nginx.conf /etc/nginx/sites-enabled/default

# collect staticfiles
RUN ./manage.py collectstatic --no-input

# container metadata
ENTRYPOINT ["/app/src/docker/entrypoint.sh"]
CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf", "-u", "root"]
ENV LANG='en_US.UTF-8'
# http
EXPOSE 8000/tcp
# uwsgi
EXPOSE 3003/tcp
VOLUME /app/media
