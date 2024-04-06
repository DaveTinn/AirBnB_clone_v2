#!/usr/bin/python3
"""
A Fabric script that distributes
an archive to web_server using do_deploy.
"""

from fabric.api import env, put, run
import os.path

env.hosts = ['54.158.182.245', '54.146.93.24']


def do_deploy(archive_path):
    if os.path.isfile(archive_path) is False:
        return False
    try:
        # Extracts file and dir name without ext.
        filename = archive_path.split("/")[-1]
        no_exten = filename.split(".")[0]
        path = "/data/web_static/releases/{}/".format(no_exten)
        sym_ln = "/data/web_static/current"
        # Upload archive to the /tmp/ dir on the web server
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path))
        run("tar -xzf /tmp/{} -C {}".format(filename, path))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path, path))
        run("rm -rf {}web_static".format(path))
        run("rm -rf {}".format(sym_ln))
        run("ln -s {} {}".format(path, sym_ln))
        print("New version deployed!")
        return True
    except ValueError:
        return False 
