__author__ = 'Joshua Zosky'

import FaceReaderBindCPython as FRB

a = FRB.Controller('1.1.1.1', 9090)
print a
a.create()
a.disconnect()
a.connect()
print 'done'

