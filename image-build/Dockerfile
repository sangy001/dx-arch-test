FROM python:latest

RUN wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -

ADD google-chrome.list /etc/apt/sources.list.d/google-chrome.list
ADD 70debconf /etc/apt/apt.conf.d/70debconf

RUN apt-get update \
    && apt-get install -y openjdk-11-jdk \
    && apt-get install -y allure \
    && apt-get install -y vim \
    && apt-get install -y google-chrome-stable

WORKDIR /root

RUN wget http://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_linux64.zip

RUN unzip chromedriver_linux64.zip && cp chromedriver /usr/bin/

RUN wget https://github.com/allure-framework/allure2/releases/download/2.13.9/allure-2.13.9.tgz \
	&& tar -xvf allure-2.13.9.tgz

ENV ALLURE /root/allure-2.13.9
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH ${JAVA_HOME}/bin:${PATH}:.:${ALLURE}/bin:${PATH}
ENV CLASSPATH .:${JAVA_HOME}/lib/dt.jar:${JAVA_HOME}/lib/tools.jar