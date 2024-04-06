#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive
form the contents of the web_static folder.
"""


from fabric.api import local
from time import strftime
import os


def do_pack():
    """
    Defines the function to generate a .tgz.
    """
    timenow = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        arc_name = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static".format(arc_name))
        print('web_static packed: {} -> {}Bytes'.format(arc_name,
            os.path.getsize(arc_name)))
        return arc_name
    except:
        return None
