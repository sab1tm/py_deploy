import cmd_utils, fs_utils, git_utils, docker_utils

cmd_utils.check_dependencies()

tmp_dir = fs_utils.create_tmp_dir()
print(tmp_dir)
git_utils.clone_git_repo(tmp_dir, "https://github.com/sab1tm/hello-app.git")
docker_utils.build_and_run_docker(tmp_dir)

fs_utils.remove_dir(tmp_dir)
