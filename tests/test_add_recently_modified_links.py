from utils.add_recently_modified_links import trim_title
import pytest


@pytest.mark.parametrize(
    "title",
    [
        ("index"),
        ("programming/index"),
        ("programming/web/webhooks"),
        ("programming/python/databases/sqlalchemy/wiki"),
        ("programming/python/databases/sqlalchemy/essential-sqlalchemy/index"),
    ],
)
def test_trim_title(title):
    trimmed_title = trim_title(title)
    count_slash = trimmed_title.count("/")
    assert count_slash <= 1
