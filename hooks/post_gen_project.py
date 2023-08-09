import subprocess

# Initialize the repo
subprocess.call(["git", "init"])

if {{cookiecutter.use_local_repo_credentials}}:
    subprocess.call(["git", "config", "--local", "user.name", "{{cookiecutter.Name}}"])
    subprocess.call(["git", "config", "--local", "user.email", "{{cookiecutter.email}}"])


# Add the basics
subprocess.call(["git", "add", ".gitignore", "PCB/*", "config.kibot.yaml"])
subprocess.call(["git", "commit", "-m", "\"Initial commit of empty project and git-specific files\""])
