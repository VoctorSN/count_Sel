from src.count_sel import count_sel

def test_total():
    assert count_sel([4, 4, 2, -3, 1, 4, 3, 2, 0, -5, 2, -2, -2, -5])==[14, 8, 4, [[2, 4], 3]]