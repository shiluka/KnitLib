# -*- coding: utf-8 -*-


def mkimg(filename, blobs):
    """ writes image to the disk """
    f = open(filename, "w")
    for off, data in blobs:
        f.seek(512 * off)
        f.write(''.join(data))
    f.close()
