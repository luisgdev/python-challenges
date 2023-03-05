"""
Letters sum problem:

Each letter stands for a different digit between 0 and 9.

EARTH + VENUS + URANUS = SATURN

What is the value of EARTH?
"""

from itertools import permutations
from timeit import timeit
from typing import Dict, List, Set, Tuple

WORDS: Tuple[str, ...] = ("EARTH", "VENUS", "URANUS", "SATURN")


def verify_sum(numbers: Tuple[int, ...], letters: Set[str]) -> bool:
    """
    Verify the sum, under the problem conditions.
    :param numbers: Set of digits.
    :param letters: Set of letters.
    :return: Bool indicating success or not.
    """
    table: Dict[str, int] = dict(zip(letters, numbers))
    words_as_number: List[int] = []
    for word in WORDS:
        word_digits: List[str] = []
        for letter in word:
            word_digits.append(str(table[letter]))
        words_as_number.append(int("".join(word_digits)))

    result: bool = sum(words_as_number[:-1]) == words_as_number[-1]
    if result:
        print("✔️ Solution found!")
        print(f"Table: {table}")
        print(f"Result: sum{tuple(words_as_number[:-1])} = {words_as_number[-1]}")
        print(f"Answer: {WORDS[0]} = {words_as_number[0]}")
    return result


def main() -> None:
    """
    Main function.
    :return: None
    """
    print("Calculating...")
    letters: Set[str] = set("".join(WORDS))
    # pylint: disable=unsubscriptable-object
    cases: permutations[int] = permutations(iterable=range(10), r=len(letters))
    for index, number_set in enumerate(cases):
        result: bool = verify_sum(numbers=number_set, letters=letters)
        if result:
            print(f"Permutations checked: {index+1}")
            break


if __name__ == "__main__":
    elapsed_time: float = timeit(stmt=main, number=1)
    print(f"Elapsed time: {round(elapsed_time, 2)} s")
