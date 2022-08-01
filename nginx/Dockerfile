FROM nginx:1.23

RUN rm /etc/nginx/conf.d/default.conf
COPY cgims.conf /etc/nginx/conf.d/

# create nonroot user/group
RUN useradd --create-home --shell /bin/bash --user-group cgims

# activate system user
USER cgims

# enable the conf by linking it to the sites-enabled directory:
# RUN ln -s /etc/nginx/sites-available/cgims.conf /etc/nginx/sites-enabled/