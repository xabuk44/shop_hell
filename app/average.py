def shop_sum(week_money):
    return sum(week_money)

# def shop_avg(week_money):
#     import numpy
#     return numpy.average(week_money)
#
# def shop_min(week_money):
#     return min(week_money)
#
# def shop_max(week_money):
#     return max(week_money)
#
# def shop_best3(week_money):
#     week_money.sort()
#     return week_money[4:7]
#
# shop_1_sum = shop_sum([5000, 2000, 3000, 1000, 4000, 6000, 7000])
# shop_2_sum = shop_sum([5000, 2000, 3000, 1000, 4000, 6000, 7000])
# shop_sum_list = [shop_1_sum, shop_2_sum]
# print(shop_sum_list)
#
# shop_1_avg = shop_avg([5000, 2000, 3000, 1000, 4000, 6000, 7000])
# print(shop_1_avg)
# shop_1_min = shop_min([5000, 2000, 3000, 1000, 4000, 6000, 7000])
# print(shop_1_min)
# shop_1_max = shop_max([5000, 2000, 3000, 1000, 4000, 6000, 7000])
# print(shop_1_max)
# shop_1_best3 = shop_best3([5000, 2000, 3000, 1000, 4000, 6000, 7000])
# print(shop_1_best3)
#
# shop_1 = [5000, 2000, 3000, 1000, 4000, 6000, 7000]
# shop_2 = [4000, 2000, 3000, 1000, 4000, 6000, 7000]

# shop_1_sum = shop_sum([5000, 2000])
# shop_2_sum = shop_sum([2000, 5000])
# shop_3_sum = shop_sum([1000, 2000])
# shop_sum_all = [shop_1_sum, shop_2_sum, shop_3_sum]
# max_sum = max(shop_sum_all)
# print(max_sum)

def shop_max(shop_sum):
    for objname,oid in globals().items():
        if oid is shop_sum:
            return objname

def shop_money(week_money):
    a = sum(week_money)
    week_money.sort()
    import numpy
    b = numpy.average(week_money)
    return a, b, min(week_money), max(week_money), week_money[4:7]

shop_1_sum = sum([5000, 2000])
shop_2_sum = sum([5000, 2000])
shop_3_sum = sum([1000, 2000])
shop_sum_all = [shop_1_sum, shop_2_sum, shop_3_sum]

print(shop_max(max(shop_sum_all)))