FROM python:3.11

# Download precompiled ttyd binary from GitHub releases
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://github.com/tsl0922/ttyd/releases/download/1.7.7/ttyd.x86_64 -O /usr/bin/ttyd && \
    chmod +x /usr/bin/ttyd && \
    apt-get remove -y wget && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

ENV NVM_DIR /root/.nvm

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash \
    && . "$NVM_DIR/nvm.sh" \
    && nvm install node \
    && nvm use node

    # install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

# Keep the container running
#CMD ["tail", "-f", "/dev/null"]

COPY . ./

#RUN ./setupenv.sh

#docker build -t crewai .

#CMD ["python", "./main.py"]
EXPOSE 7681
CMD ["ttyd", "-W", "bash"]