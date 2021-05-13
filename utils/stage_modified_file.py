import subprocess


def stage_file(file: str) -> None:
    command = ["git", "add", file]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    result_str = (result.stdout).decode("utf-8")
