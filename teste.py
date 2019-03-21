import pytest
from principal import soma

def test_soma():
    assert soma(2,4) == 6
    assert soma(8, -4) == 4
    assert soma(0, 0) == 0

test_soma()