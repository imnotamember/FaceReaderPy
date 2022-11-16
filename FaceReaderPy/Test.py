__author__ = 'Joshua Zosky'

if __name__ == "__main__":
    import __init__

import FaceReaderBindCPython as FaceReaderBinding

# Instantiate the controller with IP address(string) and Port number(integer)
a = FaceReaderBinding.Controller('127.0.0.1', 9090)
print(a)

# Check if the controller is instantiated and has an IP address and Port number
a.check()

# Disconnect from FaceReader (This should say it is not connected yet)
a.disconnect()

# Connect to FaceReader
a.connect()

# Disconnect from FaceReader
a.disconnect()
print('done')
# quit(0)
