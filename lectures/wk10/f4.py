def my_function(value1: str, value2: int) -> str:
    return value1 + str(value2)


value = my_function('123', 34)
print(value)


def my_function1(v1: list[any], v2: dict) -> tuple:
    return v1, v2
