#!/usr/bin/python3
""" Does deployment"""

from fabric.api import *
import os

env.hosts = ["34.204.82.8", "3.86.13.94"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Distributes archives to servers"""
    if not os.path.exists(archive_path):
        return False

    result = []

    send = put(archive_path, "/tmp")
    result.append(send.succeeded)

    basename = os.path.basename(archive_path)
    if basename[-4:] == ".tgz":
        name = basename[:-4]
    newdir = "/data/web_static/releases/" + name
    run("mkdir -p " + newdir)
    run("tar -xzf /tmp/" + basename + " -C " + newdir)

    run("rm /tmp/" + basename)
    run("mv " + newdir + "/web_static/* " + newdir)
    run("rm -rf " + newdir + "/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s " + newdir + " /data/web_static/current")

    return True
