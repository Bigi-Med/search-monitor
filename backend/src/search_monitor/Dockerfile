FROM python:3.11.0

WORKDIR /backend

# Install Chromium
RUN apt-get update && apt-get install -y chromium-driver

# Install ChromeDriver
RUN apt-get update && apt-get install -y curl unzip
# Install ChromeDriver (replace VERSION with the appropriate version)
RUN apt-get update && apt-get install -y curl unzip
RUN CHROMEDRIVER_VERSION=119.0.6045.105 && \
    curl -o /tmp/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$CHROMEDRIVER_VERSION/linux64/chrome-linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin && \
    rm /tmp/chromedriver.zip



COPY . ./

RUN pip install -r requirements-flask.txt

RUN pip install -r requirements-scrapy.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "-t","900","app:app"]