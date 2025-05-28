import subprocess

def clone_git_repo(tmpdir, url):
    try:
        subprocess.run(["git", "clone", url, tmpdir], check=True)
        print("Cloned to:", tmpdir)
    except subprocess.CalledProcessError as e:
        print("Clone failed:", e)
