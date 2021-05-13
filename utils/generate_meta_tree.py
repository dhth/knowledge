"""
Generate lists of metadata for atree_list md files (recursively), and pass them on to alfred_helpers.
To be run on each commit.
"""

import os
from typing import List
import re
from utils.stage_modified_file import stage_file


def generate_tree(walk_dir: str) -> List[str]:
    tree_list = []
    main_count = 0
    prefixes_to_be_stripped = [str(i) for i in range(10)]
    for root, _, files in os.walk(walk_dir):
        level = root.replace(walk_dir, "").count(os.sep)
        indent = " " * 4 * (level)
        if root.split("/")[-1] in [
            "assets",
            "images",
            "stylesheets",
            "javascripts",
        ]:
            continue
        tree_list.append(
            f"{indent}- "
            f"[:fontawesome-solid-folder: "
            f"{os.path.basename(root).title()}/]"
            f'(/{root.replace("docs/","")})'
        )
        subindent = " " * 4 * (level + 1)

        for filename in files:
            file_path = os.path.join(root, filename)

            if filename.endswith(".md"):
                # remove docs/ prefix
                file_path = file_path[5:]
                if not filename.endswith("index.md"):
                    # hack to remove number prefix from titles
                    filename = filename[:-3]
                    if filename[0] in prefixes_to_be_stripped:
                        filename = "-".join(filename.split("-")[1:])
                    title = filename.replace("-", " ").replace("_", " ")
                    # tree_list.append('{}{}'.format(subindent, f'{title}:{file_path[:-3]}'))
                    tree_list.append(
                        f"{subindent}- [{title.title()}](/{file_path[:-3]})"
                    )
                    main_count += 1
    tree_list[0] = tree_list[0].replace("Docs", "Home")
    tree_list[0] = tree_list[0].replace("docs", "")
    return tree_list


def insert_tree(
    tree_list: List[str], file_name: str, begin_marker: str, end_marker: str
) -> None:
    chop = re.compile(f"{begin_marker}.*?{end_marker}", re.DOTALL)

    f = open(file_name, "r")
    data = f.read()
    f.close()

    md_links_str = "\n".join(tree_list)

    updated_text = f"{begin_marker}\n-->\n\n{md_links_str}\n\n<!--\n{end_marker}"
    data_chopped = chop.sub(updated_text, data)

    f = open(file_name, "w")
    f.write(data_chopped)
    f.close()


if __name__ == "__main__":
    tree_list = generate_tree("docs")
    insert_tree(
        tree_list,
        file_name="docs/meta.md",
        begin_marker="WIKITREEBEGIN",
        end_marker="WIKITREEEND",
    )
    stage_file("docs/meta.md")
    print("Staged meta file.")
