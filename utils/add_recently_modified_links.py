from utils.get_staged_file_names import get_staged_files
import re


def insert_updated_links(updated_links, file_name, begin_marker, end_marker, limit=15):
    chop = re.compile(f"{begin_marker}.*?{end_marker}", re.DOTALL)

    f = open(file_name, "r")
    data = f.read()
    f.close()

    existing_links_str = chop.findall(data)[0]
    existing_links_list = existing_links_str.split("\n")
    existing_links = []
    for link_str in existing_links_list:
        if "](" in link_str:
            existing_links.append(link_str)

    for existing_link in existing_links:
        if not existing_link in updated_links:
            updated_links.append(existing_link)
            # print(f"[ADDED] {existing_link}")
        else:
            print(f"[SKIPPED] {existing_link}")

    updated_links = updated_links[:limit]

    md_links_str = "\n".join(updated_links)

    updated_text = f"{begin_marker}\n-->\n\n{md_links_str}\n\n<!--\n{end_marker}"
    data_chopped = chop.sub(updated_text, data)

    f = open(file_name, "w")
    f.write(data_chopped)
    f.close()


def get_staged_files_md_links(staged_files):
    md_links = []

    for f in staged_files:
        if len(f) > 0:
            f_name = f.strip()
            if f_name.endswith(".md"):
                # if not f_name.endswith("index.md"):
                md_file_link = f_name.split("docs/")[1]
                md_file_title = md_file_link.split(".md")[0]
                md_file_title_trimmed = trim_title(md_file_title)
                md_line = f"- [:fontawesome-solid-file-alt: {md_file_title_trimmed}]({md_file_link})"
                md_links.append(md_line)
    return md_links


def trim_title(title):
    count_slashes = title.count("/")
    if count_slashes <= 1:
        return title_case(title)
    separated = title.split("/")
    last_two = separated[-2:]
    return title_case("/".join(last_two))

def title_case(title):
    elements = title.split("/")
    if len(elements) > 1:
        if elements[1][0].isdigit():
            first_two = elements[1][:2]
            first_two = re.sub('\d', '', first_two).strip()
            elements[1] = f'{first_two}{elements[1][2:]}'
    return "/".join([re.sub('[-_]', ' ',
                            element).strip().title() for element in elements])



if __name__ == "__main__":
    staged_files = get_staged_files()
    updated_links = get_staged_files_md_links(staged_files)
    insert_updated_links(
        updated_links,
        "docs/index.md",
        begin_marker="RECENTLYMODIFIEDBEGIN",
        end_marker="RECENTLYMODIFIEDEND",
    )
    print("Done.")
