FROM ubuntu:latest

RUN apt-get update && \
	apt-get install -y \
	vim \
	sudo \
	python3 \
	python3-pip \
	python3-dev \
	default-libmysqlclient-dev \
	build-essential

RUN pip3 install -U pip

WORKDIR /work/web

ADD ./requirements.txt .

RUN pip3 install -r requirements.txt





