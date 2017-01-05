FROM ubuntu:14.04
MAINTAINER Otto Yiu <me@ottoyiu.com>

ARG docker_version
ARG mesos_version

LABEL Description="Docker Image of mesosphere/mesos-master with docker-engine installed."
LABEL Version="${docker_version} ${mesos_version}"
LABEL Dockerfile="https://github.com/ottoyiu/mesos-docker-image"

ENV docker_version ${docker_version}-0~trusty
ENV mesos_version ${mesos_version}

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install apt-transport-https && echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list && \
  apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

RUN apt-get -y update && apt-get -y install docker-engine=${docker_version}*

RUN echo "deb http://repos.mesosphere.io/ubuntu/ trusty main" > /etc/apt/sources.list.d/mesosphere.list && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \
  apt-get -y update && \
  apt-get -y install mesos=${mesos_version} && \
  apt-get -y clean && apt-get -y autoclean && apt-get -y autoremove && rm -rf /var/lib/apt/lists/*
