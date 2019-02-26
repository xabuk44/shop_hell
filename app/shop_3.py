def shop_money(week_money):
    sum_week = sum(week_money)
    week_money.sort()
    import numpy
    avg_week = numpy.average(week_money)
    return sum_week, round(avg_week), min(week_money), max(week_money), week_money[4:7]


shop_1 = list(shop_money([8000, 2000, 3000, 1000, 5000, 6000, 4000]))
shop_2 = list(shop_money([8000, 2000, 3000, 1000, 5000, 6000, 4000]))
shop_3 = list(shop_money([7000, 2000, 3000, 1000, 4000, 6000, 3000]))
shop_max = max(shop_1, shop_2, shop_3)

print(shop_max[0:1], shop_max[1:2], shop_max[2:3], shop_max[3:4], shop_max[4:5])
print(shop_1)
print(shop_2)
print(shop_3)

