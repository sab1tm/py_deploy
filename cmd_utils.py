import shutil

def is_installed(cmd):
    return shutil.which(cmd) is not None

def check_dependencies():
    dependencies = ["git", "docker", "java", "mvn"]
    for dependency in dependencies:
        if is_installed(dependency) == False:
            print(f"Error! {dependency.capitalize()} not found.")
