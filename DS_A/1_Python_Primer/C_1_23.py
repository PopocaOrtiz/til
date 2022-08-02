from typing import Union, Any

ERROR = "Don't try buffer overflow attacks on Python!"
r_type = Union[str, None]


def add_element(to_list: list[Any], index: int, element: Any) -> r_type:
    """
    attempts to write an element to a list, if out of bounds prints a message
    """
    try:
        to_list[index] = element
        return None
    except IndexError:
        return ERROR


if __name__ == "__main__":
    assert add_element([], 1, "val") == ERROR
    assert add_element([], 0, "val") == ERROR
    assert add_element([1, 2, 3], 0, "val") == None
    assert add_element([1, 2, 3], 2, "val") == None
