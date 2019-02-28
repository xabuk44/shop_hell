def sum_shop(shop_list):
    return sum(shop_list[1:])


def shop_avg(shop_list):
    import numpy
    avg_week = numpy.average(shop_list[1:])
    return round(avg_week)


def shop_day_max(shop_list):
    return max(shop_list[1:])


def shop_day_min(shop_list):
    return min(shop_list[1:])


def shop_top3(shop_list):
    shop_list = shop_list[1:]
    shop_list.sort()
    return shop_list[4:7]


shop_1 = ['Shop 1', 5000, 2000, 1000, 1000, 1000, 1000, 1000]
shop_2 = ['Shop 2', 4000, 2000, 1000, 1000, 1000, 1000, 500]
shop_3 = ['Shop 3', 5000, 2000, 1000, 1000, 1000, 1000, 1000]
shop_4 = ['Shop 4', 5000, 2000, 1000, 1000, 1000, 1000, 500]
all_shops = [shop_1, shop_2, shop_3, shop_4]

print('Best shop(-s) by total revenue for the week:')

all_shops.sort(key=sum_shop, reverse=True)
max_shop = all_shops[0]
for shop in all_shops:
    if sum_shop(max_shop) == sum_shop(shop):
        print(shop[0], '=', sum_shop(shop))

print('Best shop(-s) by average daily revenue:')

all_shops.sort(key=shop_avg, reverse=True)
max_avg_shop = all_shops[0]
for shop in all_shops:
    if shop_avg(max_avg_shop) == shop_avg(shop):
        print(shop[0], '=', shop_avg(shop))

print('The best daily revenue of the shop(-s) per week:')
all_shops.sort(key=shop_day_max,  reverse=True)
max_day_shop = all_shops[0]
for shop in all_shops:
    if shop_day_max(max_day_shop) == shop_day_max(shop):
        print(shop[0], '=', shop_day_max(shop))

print('Worst daily revenue of the shop(-s) per week')

all_shops.sort(key=shop_day_min)
min_day_shop = all_shops[0]
for shop in all_shops:
    if shop_day_min(min_day_shop) == shop_day_min(shop):
        print(shop[0], '=', shop_day_min(shop))

print('Top 3 best sales of each shop:')
print(shop_1[0], '=', shop_top3(shop_1))
print(shop_2[0], '=', shop_top3(shop_2))
print(shop_3[0], '=', shop_top3(shop_3))
print(shop_4[0], '=', shop_top3(shop_4))
