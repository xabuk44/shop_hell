def shop_money(week_money):
    a = sum(week_money)
    week_money.sort()
    import numpy
    b = numpy.average(week_money)
    return a, b, min(week_money), max(week_money), week_money[4:7]

shop_1 = shop_money([5000, 2000, 3000, 1000, 4000, 6000, 7000])
shop_2 = shop_money([50000, 20000, 30000, 10000, 40000, 60000, 70000])
print(shop_1)
print(shop_2)

# import numpy
# a = (1, 2, 3, 5, 6)
# b = numpy.average(a)
# print(b)