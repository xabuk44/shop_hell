def shop_sum(week_money):
    return sum(week_money)

shop_1_sum = shop_sum([5000, 2000, 3000, 1000, 4000, 6000, 7000])
shop_2_sum = shop_sum([50000, 20000, 30000, 10000, 40000, 60000, 70000])
print(shop_1_sum)
print(shop_2_sum)

def shop_avg(week_money):
    import numpy
    return numpy.average(week_money)

shop_1_avg =