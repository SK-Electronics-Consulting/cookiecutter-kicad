import subprocess

# Initialize the repo
subprocess.call(["git", "init"])

# Add the basics
subprocess.call(["git", "add", ".gitignore", "PCB/*", "config.kiplot.yaml"])
subprocess.call(["git", "commit", "-m", "\"Initial commit of empty project and git-specific files\""])
