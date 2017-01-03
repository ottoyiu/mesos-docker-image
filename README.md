mesos-docker-image
======

[![Build Status](https://travis-ci.org/ottoyiu/mesos-docker-image.svg?branch=master)](https://travis-ci.org/ottoyiu/mesos-docker-image)

Docker Image of mesosphere/mesos with docker-engine installed. Automatically built using travis-ci and nightli.es

Manual build
============

To create an image with docker 1.11.2 and mesos 1.1.0-2.0.107.ubuntu1404 run

```
docker build --build-arg docker_version=1.11.2 --build-arg mesos_version=1.1.0-2.0.107.ubuntu1404 .
```
