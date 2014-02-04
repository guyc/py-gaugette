# determine which platform we are running on.
#   expected values of platform are 
#   'raspberrypi','beaglebone'

import platform
# Determine platform based solely on the machine architecture.
#   rapsberrypi returns 'armv6l'
#   beaglebone black returns 'armv7l'
# This is adequate for the currently available hardware, but not future proof.
platform = 'beaglebone' if platform.machine() == 'armv7l' else 'raspberrypi'
