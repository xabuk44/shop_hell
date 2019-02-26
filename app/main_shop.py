def shop_money(week_money):
    a = sum(week_money)
    week_money.sort()
    import numpy
    b = numpy.average(week_money)
    return a, b, min(week_money), max(week_money), week_money[4:7]


shop_1 = shop_money([6005, 2000, 3000, 1000, 4000, 6000, 7000])
shop_2 = shop_money([4000, 2000, 3000, 1000, 4000, 6000, 7000])
shop_3 = shop_money([3000, 2000, 3000, 1000, 4000, 6000, 7000])



best_sum_shop = [shop_1[0:1], shop_2[0:1], shop_3[0:1]]
best_sum_shop = max(best_sum_shop)
best_sum_shop = ' '.join([str(i) for i in best_sum_shop])
print(best_sum_shop)

best_avg_shop = [shop_1[1:2], shop_2[1:2], shop_3[1:2]]
best_avg_shop = (max(best_avg_shop))
best_avg_shop = ' '.join([str(i) for i in best_avg_shop])
best_avg_shop = float(best_avg_shop)
best_avg_shop = int(best_avg_shop)
print(best_avg_shop)



# shop_1_sum = [5000, 2000, 3000, 1000, 4000, 6000, 7000]
# shop_2_sum = [4000, 2000, 3000, 1000, 4000, 6000, 7000]
# summa = [sum(shop_1_sum), sum(shop_2_sum)]
# summa.sort()
# print(summa)

