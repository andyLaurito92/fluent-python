from pytest import mark

from typehints_functions import show_count

@mark.parametrize("qty, expected", [
    (1, "1 word"),
    (2, "2 words")
])

def test_show_count(qty, expected):
    assert show_count(qty, "word") == expected


def test_show_count_no_words():
    assert show_count(0, "word") == "no words"

# Remember to add type hints in test as well! Otherwise mypy will not check them
def test_show_count_no_regular_words() -> None:
    got = show_count(3, "child", "children")
    assert got == "3 children"
