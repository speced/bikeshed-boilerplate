import datetime
import hashlib
from pathlib import Path
import subprocess
import os

import bikeshed


def main():
    rootPath = Path(__file__).resolve().parent.parent.parent.parent
    print(f"Root path is «{rootPath}»")
    oldManifest = bikeshed.update.Manifest.fromString(open(rootPath / "manifest-v1.kdl", "r", encoding="utf-8").read())
    newManifest = bikeshed.update.Manifest.fromPath(rootPath / "boilerplate-v1")
    for root, dirs, files in os.walk(rootPath / "boilerplate-v1", topdown=True):
        print(root, files)
    print(str(newManifest))
    if oldManifest.entries !=  newManifest.entries:
        with open(rootPath / "manifest-v1.kdl", "w", encoding="utf-8") as fh:
            fh.write(str(newManifest))
    else:
        print("Manifest didn't change; exiting.")


if __name__ == "__main__":
    main()
