import subprocess

def build_and_run_docker(path, image_name="hello-app-image", container_name="hello-app-container", port=8080):
    try:

        subprocess.run(
            ["docker", "build", "-t", image_name, "."],
            check=True,
            cwd=path
        )

        subprocess.run(
            ["docker", "rm", "-f", container_name],
            check=False,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )

        subprocess.run(
            ["docker", "run", "-d", "--name", container_name, "-p", f"{port}:{port}", image_name],
            check=True
        )

        print(f"Container '{container_name}' started on port {port}")
        return True

    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return False
