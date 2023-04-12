
import os
import sys
import pathlib
from dotenv import load_dotenv


dotenv_current_path = os.path.join(pathlib.Path().resolve(), '.env')
load_dotenv(dotenv_current_path)

DBA_USR = os.environ.get("DBA_USR")
DBA_PSSWD = os.environ.get("DBA_PSSWD")
