"""
quick hack to prepend mkdocs metadata to each file where
it does not exist
"""

import os
import sys

walk_dir = sys.argv[1]

print("walk_dir = " + walk_dir)


def line_prepender(filename, lines_to_prepend):
    with open(filename, "r+") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(lines_to_prepend + "\n\n" + content)


print("walk_dir (absolute) = " + os.path.abspath(walk_dir))
main_count = 0
for root, subdirs, files in os.walk(walk_dir):
    list_file_path = os.path.join(root, "my-directory-list.txt")

    for filename in files:
        file_path = os.path.join(root, filename)

        if filename.endswith(".md"):
            prepend_flag = False
            with open(file_path, "r") as f:
                count = 0
                for line in f:
                    if count == 0:
                        first_line = line.strip()
                    if count == 1:
                        if line.strip() == "===":
                            content = f.read()
                            stuff_to_add = f'---\ntitle: "{first_line}"\nsummary:\n---'
                            prepend_flag = True
                            main_count += 1
                            print(f"In {file_path}, {first_line} added")
                            break
                    count += 1
            if prepend_flag:
                line_prepender(file_path, stuff_to_add)
            # if main_count > 1:
            #     sys.exit()
