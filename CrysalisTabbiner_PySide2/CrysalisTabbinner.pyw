__author__ = "Konstantin Glazyrin"

from app.imports.common import *
from app.imports.crysalis.common import config as crysalis_config

from app.starter import *

def main():
    set_debugging_level(INFO)
    crysalis_config.set_debugging_level(INFO)

    app = App(sys.argv)

    app.setOrganizationName("DESY")
    app.setOrganizationDomain("photon-sciences.desy.de")
    app.setApplicationName("Crysalis Tabbin reader")

    starter = Starter()

    starter.info(sys.argv[0])

    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
