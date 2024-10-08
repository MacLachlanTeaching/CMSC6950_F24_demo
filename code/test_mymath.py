import pytest
import math as m
from mymath import sinc2d


@pytest.mark.parametrize("x,y,expected",
                         [(0, 0, 1),
                          (0, m.pi/2, 2/m.pi),
                          (3*m.pi/2, 0, -2/(3*m.pi)),
                          (3*m.pi/2, m.pi/2, (2/m.pi)*(-2/(3*m.pi)))])
def test_sinc2d(x, y, expected):
    observed = sinc2d(x, y)
    assert expected == observed


@pytest.mark.parametrize("x,y,expected",
                         [(1, 1, 0.7080734182735712),
                          (5, 0.25, -0.18979332974154567)])
def test_sinc2d_regression(x, y, expected):
    assert abs(sinc2d(x,y)-expected) < 1e-10
