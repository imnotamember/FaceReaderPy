# FaceReaderAPI bindings for Python

In order to utilize these bindings, you'll need to configure your project setup.

## Install dependencies

1. You'll need to set up the project in which you want to incorporate this package. To do this, download and install **one** of the following:
   1. [PsychoPy](https://www.psychopy.org)
   2. [OpenSesame](https://osdoc.cogsci.nl)
   3. It will work with any project using [Python](https://www.python.org) version 3.8+.
2. Setup [Python for .NET](https://pythonnet.github.io)
   1. Install the recommended copy of [.Net Framework](https://dotnet.microsoft.com/en-us/download/dotnet-framework) (anything >= 4.7.2).
3. Add the file "FaceReaderAPI.dll" from your installation of FaceReader to the folder [FaceReaderPy/Dependencies](FaceReaderPy/Dependencies)
4. Copy/Paste the entire folder [FaceReaderPy](FaceReaderPy) to your project folder.
5. Run the file [Test.py](FaceReaderPy/Test.py) and check the output for information regarding your ability to run this package.
   1. Below is the output from a successful run of the code:
   
   ```shell
   Running FaceReader-PythonBindings/FaceReaderPy/Test.py 
   # C:\\<your-project-path>\\FaceReader-PythonBindings\\FaceReaderPy
   # 127.0.0.1 9090
   # 127.0.0.1 9090
   # None
   # <FaceReaderBindCPython.Controller object at 0x10609c0a0>
   # 127.0.0.1
   # 9090
   # Doesn't exist
   # Just created FaceReaderAPI.FaceReaderController
   # There is no connection to disconnect
   # It Exists
   # Just created FaceReaderAPI.FaceReaderController
   # Disconnected
   # done
   ```
   
   2. If you see anything different, check that your FaceReader software is currently running.
   3. Another tool for troubleshooting is [FaceReaderExternalControlSample.exe](Resources/FaceReaderExternalControlSample.exe), in the Resources folder of this package.
6. Once you have successfully connected to FaceReader via the above utilities, then try using the file [Implementation.py](FaceReaderPy/Implementation.py) as a template for incorporating into your own project files.

Citation:
Zosky, J. (2015). FaceReaderAPI bindings for Python. Retrieved November 10, 2015, from https://github.com/imnotamember/FaceReader-PythonBindings
