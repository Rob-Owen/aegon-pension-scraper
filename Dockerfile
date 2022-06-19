FROM python:3.9-slim-buster as base

ENV POETRY_HOME=/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}

RUN apt-get update && apt-get install curl -y
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

WORKDIR /app

# Brower and WebDriver
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
    apt-get install ./chrome.deb -y &&\
    LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\
    echo "Installing chromium webdriver version ${LATEST}" &&\
    curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
    apt-get install unzip -y &&\
    unzip ./chromedriver_linux64.zip &&\
    rm ./chrome.deb ./chromedriver_linux64.zip

COPY poetry.lock .
COPY pyproject.toml .
COPY poetry.toml .

RUN poetry config virtualenvs.create false --local &&\
    poetry install --no-dev --no-root

COPY pension pension

ENTRYPOINT ["python", "-m", "pension"]
