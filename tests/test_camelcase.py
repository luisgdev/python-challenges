""" Test camelcase functions """

from typing import Dict, Iterable

import pytest

from camelcase import code

CAMEL_CASE_WORDS: Iterable[str] = (
    "updated",
    "cases",
    "todayCases",
    "deaths",
    "recovered",
    "todayRecovered",
    "active",
    "critical",
    "casesPerOneMillion",
    "deathsPerOneMillion",
    "tests",
    "testsPerOneMillion",
    "population",
    "oneCasePerPeople",
    "oneDeathPerPeople",
    "oneTestPerPeople",
    "activePerOneMillion",
    "recoveredPerOneMillion",
    "criticalPerOneMillion",
    "affectedCountries",
)

SNAKE_CASE_WORDS: Iterable[str] = (
    "updated",
    "cases",
    "today_cases",
    "deaths",
    "recovered",
    "today_recovered",
    "active",
    "critical",
    "cases_per_one_million",
    "deaths_per_one_million",
    "tests",
    "tests_per_one_million",
    "population",
    "one_case_per_people",
    "one_death_per_people",
    "one_test_per_people",
    "active_per_one_million",
    "recovered_per_one_million",
    "critical_per_one_million",
    "affected_countries",
)

CASES: Dict[str, str] = dict(zip(CAMEL_CASE_WORDS, SNAKE_CASE_WORDS))


@pytest.mark.parametrize(
    ("camel", "snake"),
    ((key, value) for key, value in CASES.items()),
)
def test_function(camel: str, snake: str) -> None:
    """ Test the function """
    assert code.convert_camel_to_snake(camel) == snake
