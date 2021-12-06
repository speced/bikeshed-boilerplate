import datetime
import hashlib
import os


def main():
    rootPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    createManifest(rootPath, folders=["boilerplate"])


def createManifest(path, files=None, folders=None, dryRun=False):
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

    if not dryRun:
        with open(os.path.join(path, "manifest.txt"), "w", encoding="utf-8") as fh:
            fh.write(manifest)

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
