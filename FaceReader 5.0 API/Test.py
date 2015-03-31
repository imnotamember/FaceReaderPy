__author__ = 'Joshua Zosky'

import FaceReaderBindCPython as FRB

a = FRB.Controller('1.1.1.1', 9090)
print a
a.connect()
a.connect()
print a.FR_Controller
print 'done'

