__author__ = 'Joshua Zosky'

from ctypes import *
# give location of dll
mydll = cdll.LoadLibrary("C:\\Users\\cb3-user\\Desktop\\FaceReader 5.0 API\\FaceReader 5.0 API\\FaceReaderAPI.dll")
print mydll
result1= mydll.FaceReaderController('172.98.0.1', 9090)
'''
result2= mydll.sub(10,1)
print "Addition value:-"+result1
print "Substraction:-"+result2
'''