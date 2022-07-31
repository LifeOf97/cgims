###############
# # # BUILDER
###############
FROM python:3.10-slim-buster as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


############
# # # FINAL
############
FROM python:3.10-slim-buster

# install deps
RUN apt update && apt-get -y install netcat gcc python3-dev musl-dev

# create nonroot user/group
RUN useradd --create-home --shell /bin/bash --user-group cgims

# update/upgrade pip
RUN pip install --upgrade pip

# activate system user
USER cgims

# create needed directories
ENV HOME=/home/cgims
ENV APP_HOME=$HOME/backend
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
COPY --from=builder --chown=cgims:cgims /app/wheels /wheels
COPY --from=builder --chown=cgims:cgims /app/requirements.txt .
ENV PATH="${HOME}/.local/bin:${PATH}"
RUN pip install --user --no-cache /wheels/*

# copy entrypoint.sh
COPY --chown=cgims:cgims ./entrypoint.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# copy project over
COPY --chown=cgims:cgims . $APP_HOME

ENTRYPOINT [ "/home/cgims/backend/entrypoint.sh" ]