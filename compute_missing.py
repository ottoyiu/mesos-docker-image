#!/usr/bin/env python3
import json
import re

from urllib.request import urlopen


SOURCE_DOCKER_IMAGE = "mesosphere/mesos"
DEST_DOCKER_IMAGE = "ottoyiu/mesos-docker-image"
DOCKER_VERSION = "1.10.3"

src_version_re = re.compile(r"^(\d+.\d+.\d+)-.*\.ubuntu1404")
dst_version_re = re.compile(r"^(\d+.\d+.\d+)-(\d+.\d+.\d+)$")


def get_tags_layer(docker_image, version_re, match_group_idx):
    tag_layer = dict()

    with urlopen("https://index.docker.io/v1/repositories/{}/tags".format(
            docker_image)) as response:
        resp = response.read().decode("utf-8")
        tags = json.loads(resp)

        tag_layer = {
            version_re.match(tag['name']).group(match_group_idx): tag['layer']
            for tag in tags if version_re.match(tag['name'])}

    return tag_layer


def main():
    src_tags_layer = get_tags_layer(SOURCE_DOCKER_IMAGE, src_version_re, 0)

    compare_tags = {
        "{}-{}".format(tag, DOCKER_VERSION) for tag in src_tags_layer.keys()}
    dst_tags_layer = get_tags_layer(DEST_DOCKER_IMAGE, dst_version_re, 0)
    missing_tags = compare_tags - set(dst_tags_layer.keys())
    print(" ".join(list(missing_tags)))

if __name__ == '__main__':
    main()
