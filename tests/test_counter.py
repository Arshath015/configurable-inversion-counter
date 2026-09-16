import pytest
from engine.inversion_counter import InversionCounter

@pytest.mark.parametrize(
    "input_data,expected",
    [
        ([1, 2, 3, 4, 5], 0),  # already sorted
        ([5, 4, 3, 2, 1], 10),  # reverse order, n*(n-1)/2 for n=5
        ([2, 3, 8, 6, 1], 5),  # classic example
    ],
)
def test_inversion_count(input_data, expected):
    counter = InversionCounter(input_data)
    assert counter.count() == expected

def test_edge_empty_and_single():
    assert InversionCounter([]).count() == 0
    assert InversionCounter([42]).count() == 0
