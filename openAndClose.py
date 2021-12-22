
from pathlib import Path
from types import new_class

newFile = Path( "lama.py" )
newFile.touch(exist_ok = True)
oneFile = open(newFile)

# import os.path
# weHaveFile=os.path.exists('lama.py')
# print(weHaveFile)
