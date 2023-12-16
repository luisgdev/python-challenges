""" Challenge """


def convert_camel_to_snake(word: str) -> str:
    """Convert camelCase to snake_case"""
    return str().join(
        "_" + char.lower() if char.isupper() else char for char in word
    )
