import sys
from pathlib import Path

import requests

try:
    needed_version = sys.argv[1]
except IndexError:
    needed_version = "1.20.4"


BUILDS_URL = "https://api.papermc.io/v2/projects/paper/versions/{}/builds"
DOWNLOAD_URL = "https://api.papermc.io/v2/projects/paper/versions/{}/builds/{}/downloads/{}"

_root = Path(__file__).parent


obj = requests.get(BUILDS_URL.format(needed_version)).json()

# Find latest build
latest_build = None
for build in obj["builds"]:
    if latest_build is None or latest_build["build"] < build["build"]:
        latest_build = build


build = latest_build["build"]
filename = _root / 'mc' / latest_build["downloads"]["application"]["name"]
filename.parent.mkdir(parents=True, exist_ok=True)

if not filename.exists():
    with open(filename, "wb") as fp:
        fp.write(requests.get(DOWNLOAD_URL.format(needed_version, build, filename.name)).content)

assert filename.exists()
assert filename.stat().st_size > 0

