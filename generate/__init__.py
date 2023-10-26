import datetime
import hashlib
from pathlib import Path
import subprocess
import os


def main():
    rootPath = Path(__file__).resolve().parent.parent
    oldManifest = open(rootPath / "manifest.txt", "r", encoding="utf-8").read()
    newManifest = createManifest(rootPath, folders=["boilerplate"])
    if(manifestsDiffer(oldManifest, newManifest)):
        with open(rootPath / "manifest.txt", "w", encoding="utf-8") as fh:
            fh.write(newManifest)
        subprocess.check_call(f"git commit -m 'Update manifest' '{rootPath/'boilerplate'}' '{rootPath/'manifest.txt'}'")
        subprocess.check_call()
    else:
        print("Manifest didn't change; exiting.")


def manifestsDiffer(old, new):
    old = old.split("\n", maxsplit=1)[1]
    new = new.split("\n", maxsplit=1)[1]
    return old != new


def createManifest(path, files=None, folders=None):
    """Generates a manifest file for all the data files."""
    if files is None:
        files = []
    if folders is None:
        folders = []
    manifests = []
    for absPath, relPath in getDatafilePaths(path):
        if relPath in files:
            pass
        elif relPath.partition("/")[0] in folders:
            pass
        else:
            continue
        with open(absPath, encoding="utf-8") as fh:
            manifests.append((relPath, hashFile(fh)))

    manifest = str(datetime.datetime.utcnow()) + "\n"
    for p, h in sorted(manifests, key=keyManifest):
        manifest += f"{h} {p}\n"

    return manifest


def keyManifest(manifest):
    name = manifest[0]
    if name.count("/") > 1:
        return 1, name
    else:
        return 0, len(name), name


def hashFile(fh):
    return hashlib.md5(fh.read().encode("ascii", "xmlcharrefreplace")).hexdigest()


def getDatafilePaths(basePath):
    for root, dirs, files in os.walk(basePath):
        if "readonly" in dirs:
            continue
        for filename in files:
            if filename == "":
                continue
            filePath = os.path.join(root, filename)
            yield filePath, os.path.relpath(filePath, basePath)


if __name__ == "__main__":
    main()
