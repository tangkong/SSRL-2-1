import databroker
from ophyd.sim import det, motor
from bluesky import RunEngine
from bluesky.plans import count, ramp_plan
from bluesky.plan_stubs import mvr, trigger_and_read

db = databroker.Broker.named('temp')
RE = RunEngine()
RE.subscribe(db.insert)

print('running plan')
from ssrltools.plans import wiggle_plan

RE(wiggle_plan([det], motor, 5))
