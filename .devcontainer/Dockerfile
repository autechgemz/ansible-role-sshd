ARG VARIANT=3.12-bookworm
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

ARG DEBIAN_FRONTEND=noninterractive

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update \
    && apt-get install -y \
    tzdata \
    ca-certificates \
    curl \
    unzip \
    lsb-release \
    git \
    gnupg \
    less \
    direnv \
    procps \
    file \
    dnsutils \
    jq \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && echo 'eval "$(direnv hook bash)"' >> ~/.bashrc \
    && echo 'eval "$(direnv hook bash)"' >> ~/.bash_profile \
    && pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt
