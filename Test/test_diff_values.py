from src.count_sel import count_sel

def test_diff_values():
    assert count_sel([-3, -2, -1, 3, 4, -5, -5, 5, -1, -5])[1]==7