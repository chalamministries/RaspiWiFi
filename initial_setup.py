import os
import sys
import setup_lib
if os.getuid():
    sys.exit('You need root access to install!')
setup_lib.install_prereqs()
setup_lib.copy_configs()
os.system('reboot')
