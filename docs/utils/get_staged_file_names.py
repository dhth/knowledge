#! usr/bin/env python

# Copies a list of staged files to system clipboard
# Inspired by https://github.com/nikitavoloboev/gitupdate

import subprocess


def get_staged_files():
    command = ["git", "diff", "--name-only", "--cached"]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    staged_files_str = (result.stdout).decode("utf-8")

    staged_files = staged_files_str.split("\n")
    return staged_files


def get_staged_file_names(staged_files):
    res_files = []

    for f in staged_files:
        if len(f) > 0:
            f_name = f.strip()
            if f_name.endswith(".md"):
                if f_name.endswith("index.md"):
                    f_name_stripped = f_name.split("/")[-2]
                else:
                    f_name_stripped = f_name.split("/")[-1].split(".")[0]
                res_files.append(f_name_stripped)

    res_files_unique = list(set(res_files))

    res_files_unique_str = " ".join(res_files_unique)

    copy_command = f'echo "{res_files_unique_str}" | pbcopy'

    # https://stackoverflow.com/questions/41238273/execute-shell-command-with-pipes-in-python

    # Copy changed file names to system clipboard

    p = subprocess.Popen(
        copy_command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    print(res_files_unique_str)


if __name__ == "__main__":
    staged_files = get_staged_files()
    get_staged_file_names(staged_files)
