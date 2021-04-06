""" 
suspender.py

callbacks that suspend operation (beam low, )
"""

from ..framework import RE
from ..devices.misc_devices import I1
from ..plans import tablev_scan

from bluesky.suspenders import SuspendFloor

susp_tablev = SuspendFloor(I1, 
                            suspend_thresh=0.1,
                            resume_thresh=0.5,
                            sleep=20
                            tripped_message='I1 dropped below threshold',
                            pre_plan=tablev_scan)

RE.install_suspender(tablev_suspender)