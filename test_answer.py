import answer

def test_add():
    assert (add(1, 2) == 3)
    assert (add(1, 1) == 2)
    assert (add(100, 200) == 300)
    assert (add(0, 1) == 1)
    assert (add(-1, 1) == 0)
