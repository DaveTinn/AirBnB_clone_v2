#!/usr/bin/python3
"""
Creates and distributes an archive
to web servers, using the function deploy.
"""


import os.path
from fabric.api import local, env, put, run
from time import strftime

env.hosts = ['54.158.182.245', '54.146.93.24']


def do_pack():
    """Generates a .tgz archive contents of a folder."""
    time = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        file_name = ("versions/web_static_{}.tgz".format(time))
        local("tar -cvzf {} web_static/".format(file_name))
        return file_name
    except ValueError:
        return None


def deploy(archive_path):
    """Deploys archive created to web servers."""
    if not os.path.isfile(archive_path):
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

    def deploy():
        archive_path = do_pack()
        if archive_path is None:
            return False
        done = do_deploy(archive_path)
        return done
