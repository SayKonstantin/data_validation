import pytest

from output_data import output_data
import json


def test_equal():
    with open('result.json', 'r', encoding='UTF-8') as file:
        res = json.load(file)

    assert res == output_data


if __name__ == '__main__':
    pytest.main()
