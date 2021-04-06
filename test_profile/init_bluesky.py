import os, sys

# Logging file ---------------------------------------------------------------
import logging

_log_path = os.path.join(os.getcwd(), ".logs")
if not os.path.exists(_log_path):
    os.mkdir(_log_path)

CONSOLE_TO_FILE = os.path.join(_log_path, 'ipython_console.log')

# start logging console to file
from IPython import get_ipython
_ipython = get_ipython()
_ipython.magic(f'logstart -o -t {CONSOLE_TO_FILE} rotate')

# create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# logging.basicConfig(filename='ex.log', level=logging.DEBUG)

logger.info('#'*60 + " startup")
logger.info('logging started')
logger.info(f'logging level = {logger.level}')

# MD Path setup --------------------------------------------------------------

def get_md_path():
    md_dir_name = "Bluesky_RunEngine_md"
    if sys.platform == "win32":
        home = os.environ["LOCALAPPDATA"]
        path = os.path.join(home, md_dir_name)
    else:       # at least on "linux"
        home = os.environ["HOME"]
        path = os.path.join(home, ".config", md_dir_name)
    return path

old_md = None
md_path = get_md_path()

if not os.path.exists(md_path):
    logger.info(
        "New directory to store RE.md between sessions: %s", 
        md_path)
    os.makedirs(md_path)
    from bluesky.utils import get_history
    old_md = get_history()

from bluesky import RunEngine
RE = RunEngine()
from bluesky.utils import PersistentDict 
RE.md = PersistentDict(md_path)
if old_md is not None:
    logger.info('migrating RE.md storage to PersistentDict')
    RE.md.update(old_md)

# keep track of callback subscriptions
callback_db = {}
