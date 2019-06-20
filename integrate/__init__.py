def my_function() -> None:
    # TODO
    # ^ who knows why this is here?
    pass


def my_function_noqa() -> str:
    return "bad TODO can be ignored with"  # noqa: T400


# This comment has both TODO and XXX
