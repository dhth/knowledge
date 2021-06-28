import os
import pathlib

import os
import sys

walk_dir = sys.argv[1]


def check_file(file_path: pathlib.Path) -> None:
    count = 0
    with open(file_path) as in_file:
        for line in in_file:
            if count == 1:
                if not line.strip() == "===":
                    print(file_path)
                break
            count += 1


if __name__ == '__main__':
    # path = pathlib.Path("docs/programming/aws/cdk/ecs/ecs.md")
    # update_link_for_file(file_path=path)
    for root, subdirs, files in os.walk(walk_dir):

        for filename in files:
            file_path = os.path.join(root, filename)

            if filename.endswith(".md"):
                path = pathlib.Path(file_path)
                check_file(file_path=path)
