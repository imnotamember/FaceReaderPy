__author__ = 'Joshua Zosky'

import FaceReaderBindCPython as FRB

## Instantiate the controller with IP address(string) and Port number(integer)
a = FRB.Controller('127.0.0.1', 9090)

## Connect to FaceReader
a.connect()

## Turn on State Logging(This is a toggle, True = Turn it on, False = Turn it off)
a.state_logging(True)

## Check for state logging events periodically, you'll want this somewhere in a trial loop
i = 0
for i in range(10000):
    if a.state_log != "":
        print a.state_log

## Disconnect from FaceReader
a.disconnect()
print 'done'