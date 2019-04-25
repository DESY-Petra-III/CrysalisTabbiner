__author__ = "Konstantin Glazyrin"

"""
This file demonstrates a simple reading from the data file
We read number, coordinates on the image, intensity, group and the frame number
"""

from app.imports.crysalis.common.config import *
from app.imports.crysalis.controller import *

def main():
    set_debugging_level(INFO)

    c = CrysalisController()
    tc = c.getTabbin()
    tc.read_file("_tests/raw/test_c1_clean.tabbin", binning=1.)
    tc.info("Total number of points is ({})".format(len(tc.points)))

    output = "\n#\tpx\tpy\tintensity\tgroup\tframe\n"

    for (i, el) in enumerate(tc.points):
        if el.group == 2:
            output += "{}\t{}\t{}\t{}\t{}\t{}\n".format(
                el.number,
                el.px, el.py,
                el.intensity,
                el.group,
                el.frame
            )
    tc.info(output)

    tc.info("Keeping track of stripes in Y direction (>1):")
    ymax = 0
    for (k,v) in tc.points_framey_ref.items():
        if len(v)>1:
            # return the number of pixels which take the same row on the same frame
            tc.info("Frame+PY:Number ({}:{}) ".format(k, len(v)))

        if len(v) > ymax:
            ymax = len(v)
    tc.info("Maximum number of points per frame with the same row ({})\n".format(ymax))

    tc.info("Keeping track of stripes in X direction (>1):")
    xmax = 0
    for (k,v) in tc.points_framex_ref.items():

        if len(v) > 1:
            # return the number of pixels which take the same row on the same frame
            tc.info("Frame+PX:Number ({}:{}) ".format(k, len(v)))

        if len(v) > xmax:
            xmax = len(v)
    tc.info("Maximum number of points per frame with the same column ({})\n".format(xmax))

if __name__ == "__main__":
    main()
