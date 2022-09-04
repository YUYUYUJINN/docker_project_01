
FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY app.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/\
    && rm /etc/nginx/conf.d/default.conf


CMD ["nginx", "-g", "daemon off;"]
