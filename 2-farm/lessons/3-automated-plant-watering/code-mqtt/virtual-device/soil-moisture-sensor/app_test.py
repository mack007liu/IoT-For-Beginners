from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

import time
from counterfit_shims_grove.grove_relay import GroveRelay

relay = GroveRelay(5)

relay.on()
time.sleep(3)
relay.off()