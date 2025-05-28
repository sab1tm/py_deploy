import subprocess

def build_maven_project(path):
    try:
        subprocess.run(
            ["mvn", "clean", "package", "-DskipTests"],
            check=True,
            cwd=path
        )
        print(f"Build successful in: {path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
