__author__ = "Konstantin Glazyrin"

"""
This file demonstrates a simple reading, filtering and writing
of the updated file format.
"""


from app.imports.crysalis.common.config import *
from app.imports.crysalis.controller import *

def main():
    set_debugging_level(DEBUG)

    c = CrysalisController()
    tc = c.getTabbin()
    tc.read_file("_tests/raw/enst_s0_peakhunt.tabbin", binning=1.)
    tc.mod_list_pixelmultiframe("_tests/output.tabbin",
                                  group=5, radius=10, frame_threshold=5)

if __name__ == "__main__":
    main()
