FROM            wps9thmango/mango:base
ENV             DJANGO_SETTINGS_MODULE  config.settings.production

COPY            ./      /srv/project
WORKDIR         /srv/project



WORKDIR         /srv/project/app


RUN             rm -rf /etc/nginx/sites-available/* && \
                rm -rf /etc/nginx/sites-enabled/* && \
                cp -f  /srv/project/.config/app.nginx \
                       /etc/nginx/sites-available/ && \
                ln -sf /etc/nginx/sites-available/app.nginx \
                       /etc/nginx/sites-enabled/app.nginx


RUN             cp -f  /srv/project/.config/supervisord.conf \
                       /etc/supervisor/conf.d/


EXPOSE          80

CMD             supervisord -n

