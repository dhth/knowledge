import os
import sys
import pathlib

import os
import sys

walk_dir = "javascript"


def update_link_for_file(file_path: pathlib.Path) -> None:
    with open(file_path) as in_file:
        f_lines = in_file.read().split("\n")
    for i,line in enumerate(f_lines):
        if "index.md)" in line:
            f_path = line.split("](")[-1].split("/index.md)")[0]
            f_lines[i] = f'- [[{f_path}]]'
        elif ".md)" in line:
            f_path = line.split("](")[-1].split(".md)")[0]
            f_lines[i] = f'- [[{f_path}]]'

    lines_to_write = "\n".join(f_lines)
    with open(file_path, "w") as f:
        f.write(lines_to_write)


if __name__ == '__main__':
    # path = pathlib.Path("docs/programming/aws/cdk/ecs/ecs.md")
    # update_link_for_file(file_path=path)
    for root, subdirs, files in os.walk(walk_dir):

        for filename in files:
            file_path = os.path.join(root, filename)

            if filename.endswith(".md"):
                print(file_path)
                path = pathlib.Path(file_path)
                update_link_for_file(file_path=path)
