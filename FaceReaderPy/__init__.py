import sys
from pathlib import Path
import clr

CWD = Path.cwd().resolve()
print(CWD)
if CWD.parts[-1] == 'FaceReaderPy':
    DEPENDENCIES = CWD.joinpath("Dependencies").resolve()
    sys.path.insert(0, str(DEPENDENCIES))
    clr.AddReference("FaceReaderAPI")  # Load the FaceReaderAPI.dll from the Python DLL's folder
else:
    print("Path 'Dependencies' not found, did you copy the entire folder 'FaceReaderPy' into your project?")
    quit(1)
