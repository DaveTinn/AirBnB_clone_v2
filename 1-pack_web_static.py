#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive
form the contents of the web_static folder.
"""


from fabric.api import local
from time import strftime


def do_pack():
    """
    Defines the function to generate a .tgz.
    """
    timenow = strftime("%Y%M%d%H$M$S")
    try:
        local("mkdir -p versions")
        archname = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(archname))
        return archname
    except:
        return None
