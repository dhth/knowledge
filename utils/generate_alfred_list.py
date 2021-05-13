"""
Generate lists of metadata for all md files (recursively), and pass them on to alfred_helpers.
To be run on each commit.
"""

import os
from alfred_helpers.script_filter import generate_json_file_with_options

walk_dir = "docs"


def generate_list():
    arg_list = []
    title_list = []
    main_count = 0
    for root, _, files in os.walk(walk_dir):

        for filename in files:
            file_path = os.path.join(root, filename)

            if filename.endswith(".md"):
                # remove docs/ prefix
                file_path = file_path[5:]
                if filename.endswith("index.md"):
                    file_path = file_path[:-9]
                    filename = file_path.split("/")[-1]
                    if file_path:
                        title = filename.replace("-", " ").replace("_", " ")
                        title_list.append(title)
                        arg_list.append(file_path)
                        main_count += 1
                else:
                    # hack to remove number prefix from titles
                    # and autocomplete suggestions
                    # since alfred doesn't do fuzzy search for
                    # script filter input
                    filename = filename[:-3]
                    if filename.startswith("0") or filename.startswith("1"):
                        filename = "-".join(filename.split("-")[1:])
                    title = filename.replace("-", " ").replace("_", " ")
                    title_list.append(title)
                    arg_list.append(file_path[:-3])
                    main_count += 1
    generate_json_file_with_options(
        arg_list=arg_list,
        title_list=title_list,
        autocomplete_list=title_list,
        subtitle_list=arg_list,
        file_path=f'{os.environ["WIKI_DIR"]}/alfred_list.json',
    )


if __name__ == "__main__":
    generate_list()
