FROM node:16

ENV DEBIAN_FRONTEND=noninteractive \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

ARG WORKDIR=/app/template

RUN mkdir -p /app && \
    mkdir -p "$WORKDIR"

WORKDIR "$WORKDIR"

COPY ./package.json ./package.json
COPY ./yarn.lock ./yarn.lock
COPY ./ ./

RUN yarn install && yarn build && rm -rf node_modules/

WORKDIR "$WORKDIR"/build

ENTRYPOINT ["/app/template/entrypoint.sh"]
