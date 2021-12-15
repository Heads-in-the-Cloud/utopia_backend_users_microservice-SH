# syntax=docker/dockerfile:1

FROM library/utopia_base

COPY . /app
WORKDIR /app

EXPOSE 5000