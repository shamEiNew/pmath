from pymath.numtheory import continued_fraction

def test_values():
    assert continued_fraction("22/5") == [4, 2, 2]