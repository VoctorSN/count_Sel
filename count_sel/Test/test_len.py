from src.count_sel import count_sel

def test_len():
    assert count_sel([-3, -2, -1, 3, 4, -5, -5, 5, -1, -5])[0]==10