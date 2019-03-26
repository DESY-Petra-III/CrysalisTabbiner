from app.imports.common import *
from app.imports.crysalis.common import config as crysalis_config

from app.starter import *

def main():
    set_debugging_level(INFO)
    crysalis_config.set_debugging_level(INFO)

    app = App(sys.argv)
    starter = Starter()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
