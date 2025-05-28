import shutil
import tempfile
import os

def create_tmp_dir():
    tmpdir = tempfile.mkdtemp()
    return tmpdir

def remove_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Directory removed: {path}")
    else:
        print(f"Directory not found: {path}")
