FROM openjdk:11-slim

# Install Chromium and its dependencies
RUN apt-get update \
    && apt-get install -y chromium \
    && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN apt-get update \
    && apt-get install -y wget \
    && wget -O /usr/local/bin/chromedriver https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && chmod +x /usr/local/bin/chromedriver \
    && rm -rf /var/lib/apt/lists/*

# Set up your application dependencies and code
# ...

CMD ["/bin/bash"]
