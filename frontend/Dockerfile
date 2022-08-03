# this dockerfile serves our vuejs app via nginx
# and also serves as a reverse proxy for our django api

####################
# Build vuejs app
####################
FROM node:buster-slim as build-vue

# create nonroot user/group
RUN useradd --create-home --shell /bin/bash --user-group cgims
USER cgims

RUN mkdir -p /home/cgims/frontend

WORKDIR /home/cgims/frontend

COPY --chown=cgims:cgims package.json .
COPY --chown=cgims:cgims package-lock.json .
RUN npm install

COPY --chown=cgims:cgims . .

# build app
RUN npm run build


####################################
# build nginx with vue app embedded
####################################
FROM nginx:1.23

# copy over conf files
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

WORKDIR /app

# set permissions for nginx user
RUN chown -R nginx:nginx /app && chmod -R 755 /app && \
    chown -R nginx:nginx /var/cache/nginx && \
    chown -R nginx:nginx /var/log/nginx && \
    chown -R nginx:nginx /etc/nginx/conf.d

RUN touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid

# copy over already built vue app
COPY --from=build-vue --chown=nginx:nginx \
    /home/cgims/frontend/dist /app/frontend/dist

# set system user
USER nginx