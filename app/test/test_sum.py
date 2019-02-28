from app.shop_sum import sum_shop


def test_sum():
    result = sum_shop(['Shop 1', 5000, 2000, 1000, 1000, 1000, 1000, 1000])
    assert 12000 == result

